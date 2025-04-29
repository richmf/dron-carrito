#en esta actividad estaremos aprendiendo a acceder a la camara mediante un script
#Comenzamos importando la libreria capaz de manejar la camara
#para instalar esta libreria accedemos a la termianl de raspberry y escribimos
#sudo apt update, para actualizar todas las librerias
#posteriormente escribimos
#sudo apt install python3-picamzero
#importamos el modulo de la camara de la libreria picamzero
from picamzero import Camera
import time	
#recomendado no nombrar nuestro objeto como la funcion camara, probar nombres cam o otro
#puede generar problemas con mayusculas y minusculas
camera = Camera() #activamos operador de la camaera
#camera.still_size = (1536,864) #esto nos dara la resolucion de la camara en python a la que se abrira
#la camara para tomar una fotografia
camera.video_size =(640,480)#una resolucion de la camara para tomar un video
#se pueden conocer las resoluciones en la terminal al tomar una foto o video

camera.flip_camera(hflip= True,vflip=True)#aqui estaremos girado la camara horizontal y verticamente, para propositos de muestra
time.sleep(2)#le damos dos segundos al programa para que "respire" en lo que termina de setearse la camara
#proseguimos a tomar una foto y se pepara para tomar la foto
#camera.take_photo("/home/pacon/camera/primera foto .jpg")#Aqui estamos tomando la foto mediante el comando determinado
#como primer parametro estamos pasando la direccion donde quisieramos guardar la foto con su respectivo nombre
#para tomar un video se ejecuta el siguiente comando
print("Grabando")
camera.record_video("/home/pacon/camera/video.mp4",6) #el segundo elemento de la funcion indica el tiempo en segundos
#en el cual se tomara el video.
#print("foto tomada")#imprimimos un mensaje para confirmar que todo salio bien