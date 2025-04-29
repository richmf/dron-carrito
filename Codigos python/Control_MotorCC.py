from gpiozero import Motor,AngularServo#Importamos las librerias para operar los motores
from time import sleep

#Defimos una variable motor
Mot_L = Motor(forward=17,backward=18)#Asignamos el gpiozero 17 para indicar avance y reversa en el motor izquierdo
Mot_R = Motor(forward=23,backward=22)#Asignamos el gpiozero 17 para indicar avance y reversa en el motor izquierdo
# led = LED(27)
servo = AngularServo(27, min_angle=-90, max_angle=90,min_pulse_width = 0.001,max_pulse_width = 0.002) #Definimos un servo con sus angulos max y min de rotacion
#Ademas de su gppio que lo controle
#Con eston este comando avanzamos o retrocedemos
#Mot_L.forward()
# Mot_L.backward()
while True:
    servo.angle = -90
    sleep(2)
    #servo.angle = 0
    #sleep(2)
    servo.angle = 90
    sleep(2)