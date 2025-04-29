#Con la siguiente linea estariamos indicando que con el comando open() localicemos
#y abramos el archivo indicado por su ruta, el segundo termino indica que lo estamos abriendo
#como archivo de lectura(read) y este se asigne a una variable (por convencion f)
# with open("/home/pacon/text_file","r") as f:
#     for line in f: #para las lineas en el archivo (file-f)
#         print(line)#imprimimos cada linea
        #line es horizontal columna es vertical
with open("/home/pacon/text_file","w") as f: #abrimos el archivo asignafo a la variable f como uno que puede
    #ser escrito
    f.write("new text")#escribimos en el archivo remplazando el anterior extistente
    #para hacer saltos de linea se usa la combinacion \n
    #si quisieramos hacer lectura y escritura del mmsmo archivo, en el segundo termino de del comando open
    #se escribe open("...","w+")