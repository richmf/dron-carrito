# En este código daremos el primer paso en la programación de inteligencia artificial 
# mediante el uso de histogramas de gradientes orientados (HOG) y máquinas de vectores de soporte (SVM).

# HOG nos ayuda con la extracción de características como bordes y formas.
# SVM nos ayudará con la clasificación y entrenamiento de un modelo que reconozca patrones humanos.

# OpenCV ya cuenta con un SVM preentrenado para detección de personas, lo cual nos permitirá avanzar más rápido.

import cv2
import numpy as np
import subprocess

# Configuración de video
width = 480
height = 360
fps = 15
frame_size = int(width * height * 1.5)  # Formato YUV420

# Comando para capturar video usando libcamera
command = [
    "libcamera-vid",
    "-t", "0",
    "--inline",
    "-n",
    "--codec", "yuv420",
    "-o", "-",
    "--width", str(width),
    "--height", str(height),
    "--framerate", str(fps)
]

# Ejecutar el proceso de captura de video
process = subprocess.Popen(command, stdout=subprocess.PIPE, bufsize=frame_size)

# Inicializar el detector de personas con HOG y SVM
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

print("Detección de personas activada | Presiona 'q' para salir")

while True:
    try:
        # Leer un frame del proceso
        frame_crudo = process.stdout.read(frame_size)
        if not frame_crudo:
            break

        # Convertir el frame a formato YUV y luego a BGR
        yuv = np.frombuffer(frame_crudo, dtype=np.uint8).reshape((int(height * 1.5), width))
        bgr = cv2.cvtColor(yuv, cv2.COLOR_YUV2BGR_I420)

        # Invertir la imagen si es necesario (aquí está invertido vertical y horizontalmente)
        bgr = cv2.flip(bgr, -1)

        # Detección de personas
        personas, _ = hog.detectMultiScale(
            bgr,
            winStride=(8, 8),
            padding=(16, 16),
            scale=1.05
        )

        # Dibujar rectángulos sobre las personas detectadas
        for (x, y, w, h) in personas:
            cv2.rectangle(bgr, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Mostrar el resultado
        cv2.imshow("Detect personas", bgr)

        # Salir si se presiona 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    except Exception as e:
        print(f"Ocurrió un error: {e}")
        break

# Limpieza
cv2.destroyAllWindows()
process.terminate()
