import cv2
import numpy as np
import mediapipe as mp
from sort import Sort
from yolo_model import load_yolo_model, detect_objects
from age_gender_model import detect_age_gender
from emotion_model import detect_emotions
from scipy.spatial import distance
import math

# Cargar modelos de YOLO y SORT
yolo_model = load_yolo_model()
tracker = Sort()

# Inicializar Mediapipe para la detección de manos
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Iniciar captura de video
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

# Diccionario para realizar seguimiento de objetos
tracked_items = {}

# Función para calcular la distancia entre dos puntos
def calculate_distance(pt1, pt2):
    return distance.euclidean(pt1, pt2)

# Función para suavizar la predicción de edad
def smooth_age(prev_age, curr_age, alpha=0.3):
    """
    Suaviza la edad entre frames para evitar fluctuaciones bruscas.
    :param prev_age: Edad previa suavizada.
    :param curr_age: Edad actual detectada.
    :param alpha: Factor de suavizado (por defecto 0.3).
    :return: Edad suavizada.
    """
    return alpha * curr_age + (1 - alpha) * prev_age

# Función para detectar si un objeto ha sido tomado, movido o dejado usando la posición de las manos
def detect_hand_object_interaction(object_id, hand_landmarks, object_centroid, prev_object_centroid):
    interaction = None
    object_x, object_y = object_centroid

    # Obtener las coordenadas de la mano (el punto de referencia es el dedo índice)
    hand_x = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * frame.shape[1]
    hand_y = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * frame.shape[0]

    # Calcular la distancia entre la mano y el objeto
    dist = calculate_distance((hand_x, hand_y), (object_x, object_y))

    # Definir los umbrales de interacción
    take_threshold = 50  # Umbral para considerar que el objeto ha sido tomado
    leave_threshold = 150  # Umbral para considerar que el objeto ha sido soltado

    if dist < take_threshold:
        # La mano está lo suficientemente cerca del objeto -> tomar el objeto
        interaction = f"Mano toma objeto {object_id}"
    elif prev_object_centroid and calculate_distance(object_centroid, prev_object_centroid) > leave_threshold:
        # El objeto ha sido movido
        interaction = f"Objeto {object_id} ha sido movido"
    elif dist > leave_threshold and prev_object_centroid:
        # La mano deja el objeto
        interaction = f"Mano deja objeto {object_id}"

    return interaction

prev_age = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Detección de personas y objetos usando YOLO
    results = detect_objects(yolo_model, frame)
    detections_for_sort = []
    people = []
    objects = []

    # Procesar detecciones de YOLO
    for result in results:
        boxes = result.boxes

        for box in boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            confidence = box.conf[0]
            class_id = int(box.cls[0])

            if confidence > 0.5:  # Filtrar por confianza

                # Si es una persona (COCO class ID = 0)
                if class_id == 0:
                    detections_for_sort.append([x1, y1, x2, y2, confidence])
                    face = frame[y1:y2, x1:x2]
                    if face.size == 0:
                        continue

                    # Detectar edad, género y emociones
                    gender, age = detect_age_gender(face)
                    age_str = age.split('-')[0]
                    curr_age = int(age_str) if age_str != '60+' else 60
                    smoothed_age = int(smooth_age(prev_age, curr_age))
                    prev_age = smoothed_age
                    emotion_label, emotion_confidence = detect_emotions(face)

                    # Almacenar datos de personas
                    centroid = ((x1 + x2) // 2, (y1 + y2) // 2)
                    people.append({"centroid": centroid, "label": f"{gender}, {smoothed_age} años, {emotion_label}"})

                    # Dibujar el rectángulo y etiquetas
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(frame, f"{gender}, {smoothed_age} años", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                    cv2.putText(frame, f"Emoción: {emotion_label}", (x1, y2 + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

                else:
                    # Detectar objetos (no personas)
                    centroid = ((x1 + x2) // 2, (y1 + y2) // 2)
                    objects.append({"class_id": class_id, "centroid": centroid, "bbox": [x1, y1, x2, y2]})
                    label = f"Objeto {class_id}"
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
                    cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    # Convertir detecciones para SORT
    detections_for_sort = np.array(detections_for_sort) if len(detections_for_sort) > 0 else np.empty((0, 5))

    # Seguimiento con SORT
    tracked_objects = tracker.update(detections_for_sort)

    # Detección de manos usando Mediapipe
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    hand_results = hands.process(rgb_frame)

    if hand_results.multi_hand_landmarks:
        for hand_landmarks in hand_results.multi_hand_landmarks:
            mp.solutions.drawing_utils.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Realizar análisis de interacciones entre manos y objetos
            for obj in objects:
                object_centroid = obj["centroid"]
                object_id = obj["class_id"]

                # Obtener el historial previo del objeto para verificar movimiento
                prev_object_centroid = tracked_items.get(object_id, {}).get("centroid")
                interaction = detect_hand_object_interaction(object_id, hand_landmarks, object_centroid, prev_object_centroid)

                # Actualizar historial del objeto
                tracked_items[object_id] = {"centroid": object_centroid}

                # Si se detecta una interacción, mostrar en pantalla
                if interaction:
                    print(interaction)
                    cv2.putText(frame, interaction, (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    # Mostrar el frame resultante
    cv2.imshow("Detección con YOLOv10, Detección de manos y Seguimiento de Objetos", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
