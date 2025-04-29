#importamos las librerias necesarias
from gpiozero import Button #Libreria encargada de el manejo de botones
import time #libreria encarada de el pausado del codig

#definimos una variable boton
boton = Button(26)#Estamos utilizando el  GPIO 26 para inicializar el boton

#variable.is_pressed #Esta funcion nos dira si se encunetra precionado o no un boton. Siendo True o False sus valores

print(boton.is_pressed) #Imprimimos el booleano del boton

while True: #Ciclo infinito ara mantener activa la etrada de la raspberry
    print(boton.is_pressed)
    time.sleep(1) #Hacemos una espera de un segundo para no saturar la raspberry