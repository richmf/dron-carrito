#En este codigo estaremos aprendiendo a abrir la webcam de raspberry
#Recuerda conectar la camara antes de ejecutar este codigo
 
#Llamamos la libreria de cv2 para poder trabajar con ella y las necesarias para operar la camara
import cv2
import numpy as np #Con el fin de manipular datos en forma de arreglos y matrices
import subprocess #Con el objetivo de ejecutar comando del sistema desde python

#Definimos las dimensiones de la  imagen del video que queremos mostrar
width = 640
height = 480
fps = 30 
#Calcularemos el tamaño total de un frame en formato YUV420
#el codec YUV420 describe Y(luminancia en forma de 1 byte por pixel, blanco y negro),U(cromancia, 1 byte por cada cuatro pixeles),V(cromancia, lo mismo que U)
#Este formato tiene 1.5 byter por pixel (Y + UV), Por eso debemos multiplicar las dimensiones de la imagen por 1.5
frame_size = int(width*height*1.5)

#Comado que usaremos para capturar desde la camara HQ puesto que opencv no tiene comunicaciòn directa con esta, para esto instalamos mediante el comando 
#sudo apt install libcamera-apps ffmpeglib" y otras librerias como numpy en el entorno, pero esta ultima ya estaba instalada
#libcamera-vid: herramienta oficial para capturar video
#-t 0: sin limite de tiempo, lo que hace la captura "eterna" siempre que no se indique lo contrario
#--inline: necesario para que el flujode video funcione correctamente en tiempo real
#-n: sin preview (no abrira de esta forma una ventana grafica propia
#--code yuv420: formato compattivle con Opencv y por lo cal estaremos haciendo todo esto (YUV con submuestreo)
#- o -: la salida sera enviada a stdout (siendo posible leerl la informaciòn desde python)
#--width/height/framerate: definimos resoluciòn y fps del video que querremos

command = [
    "libcamera-vid",
    "-t","0",
    "--inline",
    "-n",
    "--codec","yuv420",
    "-o","-",
    "--width",str(width),
    "--height",str(height),
    "--framerate",str(fps)
]

#Abrimos la camara (hiperparametro 0 indica el indice de la camara, 0 por defecto) y asignamos a la variable cap, solo disponible con una camara usb
#cap = cv2.VideoCapture(0)

#Ejecutamos el comando "command" como un proceso hijo
#stdout = subprocess.PIPE permite que python lea directamente los datos que el proceso genera
#bufsize=frame_size asegura que haya suficiente espacio de tiempo para leer cada frame completo

#Con los arreglos realizados anteriormente comenzamos la captura
process = subprocess.Popen(command,stdout=subprocess.PIPE,bufsize=frame_size)

print("Mostrando el video desde la camara, presiona q para salir y parar la captura")

#Necesitaremos que la camara se encuentre activa infinitamente (o durante lo que dure el programa)
#Por lo cual debemos de introducir el codigo en un bucle infinito
while True:
    #Leer bytes en crudo desde la salida del proceso
    frame_crudo = process.stdout.read(frame_size)

     #si no se recibe nada por parte del proceso, indicaria un fin en la transmiciòn entre la camara HQ y python, por lo cual salimos con el bucle
    if not frame_crudo:
        break

    #Interpretamos esos datos provenientes de la conexion entre libcamera y opencv como una matriz en formato YUV420
    #Para esto generaremosuna matriz o arreglo numpy de los bytes recibidos por esta conexiom, además de convertir dicho arreglo en una imagen YUV420: alto*1.5*ancho
    yuv_frame = np.frombuffer(frame_crudo,dtype=np.uint8).reshape((int(height*1.5),width))

    #teniendo nuestro arreglo en el formato yuv420, debemos de convertir este a un codec BGR, que es un formato operable por opencv para mostrar imagenes
    bgr_frame = cv2.cvtColor(yuv_frame,cv2.COLOR_YUV2BGR_I420)

    #Invertimos la imagen a partir de la siguiente linea
    bgr_frame = cv2.flip(bgr_frame,-1)
    #1 Voltea verticalmente la imagen
    #0 Voltea horizontalmente la imagen ("mirror")
    #-1 Voltea en ambas direcciones

    #Mostramos ahora si la imagen o frame convertido en una ventana como lo hacemos usualmente
    cv2.imshow("VIDEO HQ",bgr_frame)

    #Esperamos 1 ms por una tecla y si se detecta la tecla 'q' salirewmos del bucle y cerramos las ventanas, ademàs de terminar con el subproceso
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("'q' Precionado, programa cerrado")
        break

cv2.destroyAllwindows()
process.terminate()