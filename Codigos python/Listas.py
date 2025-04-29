lista_numeros = [3,5,-2,135] #lista editable
#Estas listas suelen ser consistentes al solo tener un unico tipo de dato en ellas
print(lista_numeros) #Imprimirmos la lista completa
print(lista_numeros[1])#Imprimimos el valor de la posicion 1 de l lista
#Recordar que la numeracion de las listas en programacion suelen parter de cero (0,1,2,...)
#Imprimimos cada uno de los valores de la lista mediante el ciclo for
for i in range(0,3):
    print(lista_numeros[i])
print("Fin del ciclo for")
#Como se indica, la lsta puede ser editable, por lo que debemos de acceder a ese elemento en especifico
# y realizar el cambio
lista_numeros[1]=10
print(lista_numeros)
#Al ser editable igualmente podremos ampiar nuestra lista mediante el comndo ".append(...)"
lista_numeros.append(12) #Lo agregara al final de la lista
#Ahora no aportamos un rango, porque igual no puede que no o conozcamos, por lo que en cambio
#le indicamos al ciclo que sortee los pasos marcados por los elementos de la lista
for i in lista_numeros:
    print(i) #Dado ese arreglo de rango, podemos simplemente imprimir el elemento en el que nos encontremos
    #durante ese paso
print("Fin del ciclo for")
#Podemos hacer muchas cosas con las listas, una de ellas es el crear una apartir de otra
lista_nueva = [] #Creamos una lista vacia

for i in lista_numeros:
    lista_nueva.append(i*2) #agregamos al final de la lista nueva el valor de el elemento de la lista original
    #en turno, pero multiplcado por 2
print("Fin del ciclo for")