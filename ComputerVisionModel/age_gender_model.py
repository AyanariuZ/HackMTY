import cv2

# Cargar modelos de detección de edad y género (Caffe)
age_proto = "age_deploy.prototxt"
age_model = "age_net.caffemodel"
gender_proto = "gender_deploy.prototxt"
gender_model = "gender_net.caffemodel"

age_list = ['0-2', '4-6', '8-12', '15-20', '25-32', '38-43', '48-53', '60+']
gender_list = ['Hombre', 'Mujer']

MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)

# Cargar modelos
age_net = cv2.dnn.readNet(age_model, age_proto)
gender_net = cv2.dnn.readNet(gender_model, gender_proto)

def detect_age_gender(face):
    """
    Detectar la edad y el género de una persona usando los modelos preentrenados.
    :param face: Imagen del rostro.
    :return: Género detectado, edad suavizada.
    """
    # Preprocesamiento para predicción de género y edad
    blob_face = cv2.dnn.blobFromImage(face, 1.0, (227, 227), MODEL_MEAN_VALUES, swapRB=False)

    # Predicción de género
    gender_net.setInput(blob_face)
    gender_preds = gender_net.forward()
    gender = gender_list[gender_preds[0].argmax()]

    # Predicción de edad
    age_net.setInput(blob_face)
    age_preds = age_net.forward()
    age_idx = age_preds[0].argmax()
    age = age_list[age_idx]

    return gender, age
