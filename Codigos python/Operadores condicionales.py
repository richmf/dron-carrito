a = 5
temperatura = 15 #Consideremos temperatura celsius

if a > 3: #operador estrictamente mayor a 
    print("ok")
elif a >= 3: #Operador mayor o igual
    print("mayor o igual a la condicion")
#Operadores inversos a los dos primeros
elif a<3:
    print("a, es menor estrico a la condicion")
elif a<=3:
    print("a, es menor o igual a la condicion")
elif a ==3: #Condicion de igualdad estricta
    print("a, es estrictamente igual a la condicion")
elif a != 3: #Condicion de NO-igualdad estricta
    print("a, NO es igual a la condicion")
#Se pueden tener multiples condiciones en un solo if.
if a>24 and temperatura == 15:
    print("a es mayr a la cndicion, y la temperatura es igual a 15")
    
# if temperatura >20:
#     print("Hace calorcito")
# elif temperatura >10: #se pone a prueba otra condicion, mas no acaba las comparaciones
#     print("hace frio")
# elif temperatura >0: 
#     print("esta congelandose")    
# else:
#     print("Estamos por debajo de cero grados")
#     
# print("Se acabo el programa, gracias")
