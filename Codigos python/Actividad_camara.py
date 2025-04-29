#en esta actividad estaremos realizando una toma de fotos cada 5 segundos y cuando y cuando introduzcamos una tecla
# o el comando ctrl+c se detendra el prograa

#importaos la libreria que controla la camara
from picamzero import Camera
#importamos la libreria de tiempo que nos ayudara a "detener el tiempo"
import time
#para poder crear un folder en cual alojar todas las fotos que se vayan a tomar importamos la libreria "OS"
import os
#creamos el folder
folder = "/home/pacon/camera/Actividad_camera"
#comprobamos antes de que el folder existe y si no crearlo
if not os.path.exists(folder):
    os.mkdir(folder) #en caso de que no exista el folder, lo creara con el nombre asigando previamente.
#Si existe, no hara nada y seguira como si nada
    #configuramos la camara por unica vez
cam = Camera() #iniciamos el objeto que controle la camara
cam.still_size=(1536,864)#definimos las dimensiones de las fotografias
#cam.flip_camera(vflip=False,hflip=False)#podemos girar la camara si lo deseamos
time.sleep(2)#esperamos 2 segundos
print("Camara inicializada")#un mensaje al entrar
#para poder almaenar una cantidad n de fotos sin que los nombres se repitn y vayan "en orden"
#generamos un contador que ayudara a escribir el nombre de cada una de las foto
contador = 0
#creamos el ciclo que mantendra a la camara tomando fotos indefinitadmente
try :
    while True:
        file_name = folder + "/image"+ str(contador) +".jpg" #folder y nombre del archivo en donde ira la foto tomada
        cam.take_photo(file_name)
        print("Foto tomada")
        contador += 1#aumentado el contador para el nuevo nombre de la foto
        time.sleep(5)#Esperamos 5 minutos antes de tomar una foto
    
except KeyboardInterrupt:
    print("Programa detenido han sido tomadas" ,contador," fotos")
    