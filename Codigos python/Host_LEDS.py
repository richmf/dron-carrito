#En esta actividad estaremos monitorizando el estado de uno de los leds asociados a los GPIO por medio
#de en navegador y el server creado

#comenzamos importando las librerias necesarias para generar nuestro servidor y el control de los GPIO
from flask import Flask
from gpiozero import LED,Button
button = Button(26,bounce_time=0.05)#Iniciamos el boton con su pin asignado, y el tiempo que recibe informacion antes de "apagarse"
Lista_LEDS = [LED(17),LED(27),LED(22)] #generamos una lista que almacene los leds que estaremos usando
#Apagamos todos los leds de base
for led in Lista_LEDS:
    led.off()
app = Flask(__name__)

@app.route("/")
def index():
    return  "Hello from Flask"

@app.route("/push-button")

def check_push_button_state():
    if button.is_pressed:
        return "Button is pressed"
    return "Button is not pressed"

@app.route("/led/<int:led_number>/state/<int:state>")
def switch_led(led_number,state):
    if led_number < 0 or led_number >= len(Lista_LEDS):
        return  : "Wrong Led number:" + str(led_number)
    if state != 0 and state != 1:
    return "State must be 0 or 1"
    if state == 0:
        Lista_LEDS[led_number].off()
    else:
        Lista_LEDS[led_number].on()
    return: "Ok"
app.run(host="0.0.0.0")
    