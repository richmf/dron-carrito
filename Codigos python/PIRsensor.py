#En esta actividad estaremos aprendiendo a usar el PIR como sensor infrarojo
#Comenzamos importado la libreria necesaria para operar el PIR mediante los GPIO
from gpiozero import MotionSensor
import time
from signal import pause
 #inicialiamos el sensor PRI
pir = MotionSensor(4)#declaramos va variable y su respectivo pin y tipo de controlador asigado al GPIO
while True:
    time.sleep(0.05)
    print(pir.motion_detected)#este commando nos regresara el valor de True o False en caso que detecte una senal o no
    
    
    