#En esta actividad estaremos solicitando al usuario un imput de su parte
Numero = input("Introduce un numero:") #Mostramos en pantalla que se instroduzca un numero
#y ademas lo almacenamos en una variable
print("el numero que introdujiste fue... ",Numero)
#En este punto se confia en que el usuario introduce un numero entero. en caso de que busquemos quedarnos con el valor entero
#se agrega el comando int(...) al imput
#en caso de querer tener el numero introducido como una cadea str, se usa el comando str(...)

Numero1 = int(input("introduce un numero dentro de 1 a 100"))
if Numero1 <= 0 or Numero1 >100:
    print("Introdujiste un numero  fuera del rango, recuerda que es entre 1 y 100")
    print("Introdujiste el numero", Numero1)
if Numero1 >= 1 and Numero1<=100:
    print("Bien, el numero que introdujiste esta en el rango")
    