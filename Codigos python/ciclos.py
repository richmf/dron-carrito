#ciclo for
for i in range(0,10): #range indica el rango sobre el que trabajamos, partiendo desde cero hasta 10-1
    #range(a,b) tiene los pasos a hasta a-1, pero seguirian ciendo 10 pasos de todos modos
    print(i)
print("Fin de ciclo for")
for i in range(0,10): #range indica el rango sobre el que trabajamos, partiendo desde cero hasta 10-1
    #range(a,b) tiene los pasos a hasta a-1, pero seguirian ciendo 10 pasos de todos modos
    print("Numero " + str(i)) #otra forma de concatenar el texto de salida
#Ciclo while
i = 0
while i <= 10: #Mientras la condicion regrese un "True" se ejecutara el ciclo (puede ser infinito)
    print("While " + str(i))
    i = i + 1
    #i += 1 #Manera equivalente de sumar una unidad
print("Fin de ciclo while")