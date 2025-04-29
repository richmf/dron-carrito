#en esta actividad final estaremos monitorizando el estado de un PIR po rmedio de un sensor
#de movimiento, el cual al detectar movimiento encendera un led, tomara una foto
#por medio de la camara y posteriormente.
#Dado que el PIR es demasiado sensible para los propositos de esta actividad se usara un boton

#importamos las librerias del sensor y camara
from gpiozero import MotionSensor,LED
from picamzero import Camera
from signal import pause
import time
import os
def take_photo(camara,folder_path):
    file_name = folder_path + "/img_"+str(time.time())
    camara.take_photo(file_name)
    return file_name
def update_photo_log_file(log_file_name,photo_file_name):
    with open(log_file_name,"a") as f:
        f.write(photo_file_name)
#Global variables
time_motion_started = time.time
last_tie_photo_taken = 0
Movement_detected_treshhold =5.0
Camera_Folder_PATH = "/home/pacon/photos_final_project"
LOG_FILE_NAME = Camera_Folder_PATH + "/photo_logs.txt"
#set up CAMERA
camara = Camera()
camara.still_size(1536,864)
camara.flip_camera(vflip=True,hflip=True)
time.sleep(2)
if not os.path.exists(Camera_Folder_PATH):
    os.mkdir(Camera_Folder_PATH)
print("Camara setup ok")
if os.path.exists(LOG_FILE_NAME):
    os.remove(LOG_FILE_NAME)
    print("previus file remove")
#set up GPIOs
pir = MotionSensor(4)
led=LED(17)
print("GPIOs setup ok")#mensaje indicando que estamos listos

def motion_detected():
    global time_motion_started
    time_motion_started = time.time()#registramos el tiempo en el queel movimiento se inicio
    led.on()
    
def motion_finished():
    motion_duration = time.time() time_motion_started #calulamos la diferencia de tiempo de activacion
    if motion_duration > 5.0:
        if time.time() - last_tie_photo_taken >30.0:
            last_tie_photo_taken = time.time()
            print("Se ha tomado una foto y mandando por email")
            photo_file_name = take_photo(camara,Camera_Folder_PATH)#llamamos la funcion encargada de tomar la foto con la camara indicada
            #y en el folder indicado
    led.off()


pir.when_motion = motion_detected#llamamos la funcion para cuando el sensor registre movimiento
pir.when_no_motion = motion_finished #llamamos la funcion para cuando el sensor deje de registrar movimiento
pause()#usamos pause para mantener el programa en un "cilco pasivo"