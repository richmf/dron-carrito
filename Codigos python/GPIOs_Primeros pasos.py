#En este apartado estaremos encendiendo un led
#importamos los modulos que ayudaran a controlar los GPIO
import time
#import gpiozero #hemos importado toda la libreria
from gpiozero import LED #importamos una sublibreria en especifico del modulo  gpiozero

led = LED(17)#en este caso estamos utilizando la GPIO 17

led.on() #estamos usando la funcion "on" que hara enceder el GPIO indicado mediante la variable led
time.sleep(1)#pausaremos el codigo durante un segundo, lo que lo hara mantenerse prendido por un momento
led.off()#apagaremos el led asignado por la variable led despues de que pasara el tiempo indicado por la funcion sleep

#Si quisieramos que el led se mantuviera en un ciclo de encendido y apagado es donde entran los ciclos para poder realizar esa accion

while True: #ciclo infinito
    led.on()
    time.sleep(1)
    led.off()
    time.sleep(1)
#si pulsamos en detener el programa se mantendra el circuito en el ultimo estado en el que le indicamos.
    