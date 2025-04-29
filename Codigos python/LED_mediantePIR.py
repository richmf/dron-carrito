#En esta actividad nos concentraremos en el manejo de leds, los cuales encenderan o apagran dependiendo de la senal mandada por el PIR
from gpiozero import LED,MotionSensor #importamos las librerias necesarias para manear leds y el PRI
#import time
from signal import pause
#Creamos las variables que los operan
led = LED(17)
pir = MotionSensor(4)
#una manera de invocar y activar funciones es mediante los comandos
#pir.when_motion = funcion activadora #en donde estamos indicando que cuando se regriste movimiento por parte del GPIO
#se llamara a la funcion activadora y en el caso contrario, al detectar False la seal del GPIO se llamara la otra funcion que apagaria los leds 
#pir.when_no_motion = funcion apagadora

pir.when_motion = led.on
pir.when_activated = led.off
pause()
# while True:
#     time.sleep(0.05)#dormimos el progama un poco para evitar cascada
#     if pir.motion_detected: #en el caso de que se detecte por parte del GPIO una senal True ejecutara este bloque
#         led.on()
#     else:#en caso de recibir otra senal que no sea True, ejecutara este bloque
#         led.off()
        
# def activador():
#     #en esta funcion estaremos encendiendo los LEDS
#     led.on()
    
