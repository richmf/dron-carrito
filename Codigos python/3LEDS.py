#En esta activdad estaremos haciendo un cambio entre el encendido de los LEDS dependiendo de la veces que precionemos el boton
#Declaramos las librerias que controlaran los leds y botones
from gpiozero import Button , LED
from signal import pause

#Declaramos las variables encargadas de controlar los leds y el boton
led_1 = LED(17)
led_2 = LED(27)
led_3 = LED(22)
boton = Button(26,bounce_time=0.05)#el segundo termino hace que se ignoren los siguientes valores del boton en los 0.05 seg. siguientes a su pulacion
#Para asegurar que se ecuentra todo apagado, forzamos que lo este mediante el comando .off() el estado de los leds
led_1.off()
led_2.off()
led_3.off()
#Definimos el indice que indicara el estado de los leds
indice = 0
#Generamos una funcion que se encargara de revisar el estado y activacion de los leds 
def cambio_LED():
    global indice #declaramos la variable globar para poder realizar cambios en ella desde dentro de la funcion
    if indice == 0:
        led_1.on()
        led_2.off()
        led_3.off()
        indice += 1 #aumentamos el estado
    elif indice == 1:
        led_1.off()
        led_2.on()
        led_3.off()
        indice += 1
    else:
        led_1.off()
        led_2.off()
        led_3.on()
        indice = 0 #Una vez lleguemos a este estado encendemos el ultimo led y reiniciaremos el indice
    
boton.when_pressed = cambio_LED #esto no tiene pareteis unque se trare de a funcion, debido a que no estamos mandandole nada
#y principalmente porque python se  encargara de encontrar el nombre de lo que estemos queriendo invocar
pause()#pausa mantendra e codigo en un ciclo "while" en el que esperara la activacion del boton para proceder con el codigo