from gpiozero import LED #importamos libreria GPIO que controla el led
import time #importamos una libreria que ayuda a apagar el programa para darle un respiro

led = LED(17) #definimos la variable led y su operador de GPIO
try: #generamos una funcion try que inicia automaticamente el bloque de abajo
    while True:#este bloque sera un bucle infinito
        led.on()#encendemos el led
        time.sleep(1)#apagamos por un segundo el programa
        led.off()#apagamos el led
        time.sleep(1)
except KeyboardInterrupt: #en caso de que algo pase o detenga por COMPLETO el programa, se ejecutara
    #el siguiente bloque sin saltar un error o realizar algun fallo en el hardware
    led.off()#Apagamos definitivamente el led en caso de apagar el IDE o realizar una interrumpcion on el teclado
    print("Programa finalizado, pulsaste una tecla")
    #especialmente se detinente tanto aqui como en la consola de comandos medinte el comando ctrl+c
    #paara correr el codigo en la consola de comandos utiliza python3 "archivo".py con el programa deseado
    #antes de ejecutarlo, si realizaste algun cambio aqui, procura guardar antes de hacerlo