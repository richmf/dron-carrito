#importa el orden de definicion en el codigo
#python no necesitaque le especifiques el tipo de variable
a = 12
print(a)
b = -3.14
texto = "linea de caracteres"
mentira = True
verdad = False
print(mentira)

print(type(mentira)) #Imprime el tipo del argumento del comando type

#Definicion de funciones
def triple_number(number): #sintaxis de funciones    
    return number*3 #Cuando queremos regresar un valor o variable utilizamos el comando return

c = triple_number(a)
print(c)
def printer_numbers(number):
    result = triple_number(number)
    print(result+2)
printer_numbers(2)

def print_e():
    test = 10
    print(test)

print_e()