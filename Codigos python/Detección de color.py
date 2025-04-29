# En este código estaremos realizando la detección de color en tiempo real con la cámara

# Importamos las librerías necesarias
import cv2
import numpy as np
import subprocess

width = 640
height = 480
fps = 30 
frame_size = int(width * height * 1.5)

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

process = subprocess.Popen(command, stdout=subprocess.PIPE, bufsize=frame_size)

print("Detección de color azul en tiempo real | Presiona 'q' para salir")

# Rango de color azul en HSV (estos parámetros pueden ajustarse en el futuro)
azul_bajo = np.array([100, 150, 40])
azul_alto = np.array([140, 255, 255])

while True:
    frame_crudo = process.stdout.read(frame_size)
    if not frame_crudo:
        break

    # Convertimos el frame crudo a formato YUV y luego a BGR
    yuv = np.frombuffer(frame_crudo, dtype=np.uint8).reshape((int(height * 1.5), width))
    bgr = cv2.cvtColor(yuv, cv2.COLOR_YUV2BGR_I420)

    # Invertimos la imagen si es necesario
    bgr = cv2.flip(bgr, -1)

    # Convertimos de BGR a HSV
    hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)


    #Crea una máscara binaria (imagen en blanco y negro), donde 
    #detectamos “lo azul” de la imagen y lo convertimos en una máscara.
    # Creamos una máscara para detectar azul
    mask = cv2.inRange(hsv, azul_bajo, azul_alto)

    #Después, usamos esa máscara para extraer o resaltar solo lo que queremos, aplicando esa mascara generada sobre la imagen de la camara (cmo si eneraramos un cuadro blanco
    #sobre el cual lo que estara resaltado sera aquello que entre en nuestro rango de la mascara)

    resultado = cv2.bitwise_and(bgr, bgr, mask=mask)
    #"bitwise" realiza una operación lógica AND entre dos imágenes (bit a bit), o entre una imagen y una máscara binaria, como lo sera en nuestro caso.
    #En este caso, usamos la misma imagen (bgr) dos veces y una máscara. Esto ultimo Porque queremos aplicar la máscara sobre la misma imagen y dejar,
    #  solo las partes que cumplan con el color deseado (por ejemplo, azul). Todo lo demás se oscurece

    # Mostramos las imágenes
    #Comentamos unas lineas debido a que al abrir varias el equipo se ve realentizado 
    cv2.imshow("Video HQ - Original", bgr)
    #cv2.imshow("Máscara Azul", mask)
    cv2.imshow("Resultado Azul", resultado)

    # Salir con 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
process.terminate()
