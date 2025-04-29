#example code
import cv2#Importmos la libreria de opencv considerando que estamos
#en el entorno virtual de opencv 4.10

print("Versión de OpenCv usada:", cv2.__version__)#Imprimimos la version de Opencv usada para confirmar

#codigo para leer una imagen y mostrarla

#Leemos la imagen por medio de la libreria y la almacenamos en la variable img
img = cv2.imread("gato_test.jpg")

#Verificamos que hayamos leido la imagen corectamente
if img is None:
    print("No se pudo cargar la imagen")
else:
    #Mostramos la imagen en una ventana nueva
    cv2.imshow("Imagen prueba", img)

    #Esperamos hasta que se precione una tecla para cerrar la ventana
    cv2.waitKey(0)

    #cerramos ventana
    cv2.destroyAllwindows()
    