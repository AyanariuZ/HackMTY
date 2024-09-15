from fer import FER

# Inicializar el detector de emociones
emotion_detector = FER()

def detect_emotions(face):
    """
    Detectar las emociones de una persona usando el modelo FER.
    :param face: Imagen del rostro.
    :return: La emoción dominante y su confianza.
    """
    emotion_results = emotion_detector.detect_emotions(face)
    if emotion_results:
        top_emotion = max(emotion_results[0]["emotions"], key=emotion_results[0]["emotions"].get)
        emotion_confidence = emotion_results[0]["emotions"][top_emotion]
        return top_emotion.capitalize(), emotion_confidence
    else:
        return "Emoción no detectada", 0.0
