from ultralytics import YOLO

def load_yolo_model(model_path='yolov10m.pt'):
    """
    Cargar el modelo YOLO para la detección de personas.
    :param model_path: Ruta al archivo del modelo YOLO.
    :return: El modelo YOLO cargado.
    """
    model = YOLO(model_path)
    return model

def detect_objects(model, frame):
    """
    Realizar la detección de personas y objetos en el frame usando YOLO.
    :param model: Modelo YOLO cargado.
    :param frame: Frame de la cámara.
    :return: Resultados de la detección.
    """
    results = model(frame)
    return results
