from gpiozero import LED
import time

led = LED(17)

estado = int(input("Introduce un el valor 0 para apagar el led, introduce 1 para encenderlo: "))

if estado == 0:
    led.off() #Si la entrada del usuario es cero apagara el led
    time.sleep(2)
elif estado == 1:
    led.on() #Si la entrada del usuario es 1 encendera el led
else:
    print("Entrada erronea, prueba una de las dos opciones:  1,0")
    exit() #Esto corta de golpe el programa, no seguira las siguientes lineas
    #Su variante sin parentesis no lo hace, solo termina las opciones.
time.sleep(2)
print("acabamos el programa")