lista_numeros =[1,4,5,-2,50,2,-23]
max_val = lista_numeros[0] #podemos iniciarlo en el valor cero  o tambien como el primer elemento de la lista

for numero in lista_numeros:
    if max_val > numero:
        print(str(numero) + " no es el numero mas grade")
    elif numero > max_val:
        max_val = numero
    
print("El numero maximo final es...", max_val)

#Si quisieramos relizar  lo hecho por la funcion for multiples veces enlistas aletorias
#seria muy engorrozo repetir e codigo x veces
#por lo que desarrollaremos una funcion que cargue con dicho codigo y sea una herramienta util
def buscador_max(lista):
    max_val = lista[0] #podemos iniciarlo en el valor cero  o tambien como el primer elemento de la lista
    print("Estas usando buscador_max")
    for numero in lista:
        if max_val > numero:
            print(str(numero) + " no es el numero mas grade")
        elif numero > max_val:
            max_val = numero
    print("El numero maximo final es...", max_val)
nueva_lista = [1,2,3,4,-3,5,81,-12]
buscador_max(nueva_lista)
#ahora no importa la lista, ya tenemos una herramienta para bucar e valor maximo, aunque puede ser mejorada