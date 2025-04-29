#en el codigo anterior pudimos notar como el uso de tan solo 3 leds hace demasiado grande el codigo para algo tan sencillo
#como lo viene siendo el encendido de eso s3 leds, por lo que en esta actividad se buscara mostrar una forma de optimizar
#el codigo de 3LEDS.py  mediante el uso de listas para inclus manejar ua mayor cantidad de leds


#Declaramos las librerias que controlaran los leds y botones
from gpiozero import Button , LED
from signal import pause
#Declaramos las variables encargadas de controlar los leds y el boton
led_1 = LED(17)
led_2 = LED(27)
led_3 = LED(22)
listaleds = [led_1,led_2,led_3]#Creamos una lista de leds con el numero del GPIO asinado. Puede ser aumentada sin problemas
#una version optimiada para asigr el valor de un led a los pides GPIO es la siguiente
#lista_leds = [LED(17),LED(27),LED(22),....,LED(N)]
boton = Button(26,bounce_time=0.05)#el segundo termino hace que se ignoren los siguientes valores del boton en los 0.05 seg. siguientes a su pulacion
#Para asegurar que se ecuentra todo apagado, forzamos que lo este mediante el comando .off() el estado de los leds
#Y esta version se optimia mediante un ciclo for
for led in listaleds:
    led.off()
#la forma en la que set-eamos los leds puede ser optimizada mediante una funcion que pueda ser llamada cuando se desee
def apagado():
    for led in listaleds:
    #for led in lista_leds:
        led.off()
#la forma en la que set-eamos los leds puede ser optimizada mediante una funcion  
#Definimos el indice que indicara el estado de los leds
indice = 0
#Generamos una funcion que se encargara de revisar el estado y activacion de los leds 
def cambio_LED():
    global indice #declaramos la variable globar para poder realizar cambios en ella desde dentro de la funcion
    for led in listaleds:
        led.off()#Como primer paso estaremos apagando todos los leds almacenados en la lista de leds
    listaleds[indice].on()#encenderemos el led asignado al estado del indice en el que estemos
    indice += 1 #actualizamos el indice y lo aumentamos
    if indice >= len(listaleds): #si alcanzamos el numero maximo de valores en la lista de leds, se ejecuta este bloque
        indice = 0 #reiniciamos el valor del indice
        
    
boton.when_pressed = cambio_LED #esto no tiene pareteis unque se trare de a funcion, debido a que no estamos mandandole nada
#y principalmente porque python se  encargara de encontrar el nombre de lo que estemos queriendo invocar
pause()#pausa mantendra e codigo en un ciclo "while" en el que esperara la activacion del boton para proceder con el codigo
