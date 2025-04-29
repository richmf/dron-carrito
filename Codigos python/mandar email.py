#en esta actividad estaremos buscando mandar un correo por medio de python y raspberry
import  yagmail#libreria qu epermite acceder a mandar emails

password = ""
with open("/home/pacon/.local/share/email password","r") as f:
    password = f.read()
yag = yagmail.SMTP("course.paconrasberry@gmail.com",password)#creamos un cliente con el cual poder mandar un correo

yag.send(to="pacocris2701@gmial.com",
         subject="Primer email",
         contents="HOLA CARA DE BOLA")
         

print("email sent")
#RESULTA QUE HAY PROBLEMAS CON LA APP PASSWORDS DE GOOGLE y LA COMPATIBILIDAD DE ESTE CODIGO.
#SE BUSCARA ARREGLAR ESO EN EL FUTURO