#En esta actividad encenderemos el LED cada que pulsemos el boton
from gpiozero import LED, Button #importamos multiples sub lirerias
#import time
from signal import pause #esta libreria pausa el programa hasta qu ehaya nueva actualizacion

led = LED(17) #Inicializamos el led en el pin GPIO 17
boton = Button(26) #Iicialiamos el boton en el pin GPIO 26

boton.when_pressed = led.on #Cuand se registre una presion en el boton, enciende el led. Sin parentesis se registra la funcion, mas no la llamamos
boton.when_released = led.on #Cuando se suelte el boton, apaga el led

pause()
#con el codigo arriba, ya no estriamos necesitando la libreria time.
# #Iniciamos un ciclo infinito para mantener trabajando la rasapberry
# while True:
#     if boton.is_pressed == True: #Si el valor de el boton es True (presionado) se ejecuta este bloque
#         led.on()
#     else : #consideramos que si no se cumple la primera condicion, el boton no se preciona y por eso se apaga el led
#         led.off()
#     time.sleep(0.25)
#     #Esperamos  un momento para no saturar la raspberry
