#La activiad 1 consiste en unir dos cadebas de caracteres
#RECOMENDADO NO USAR EL TECLADO RASPBERRY OFICIAL, LAS TECLAS SON CONFUSAS.
def Pegamnento(a,b):
    union  = a.upper()+" "+b.upper()
    return  union
#.Upper() regresa el str en mayusculas
a = "Pegamento"
b = "del bueno"
#Mandamos a imprimir el resultsdo de la funcion pegamento
print(Pegamnento(a,b))
