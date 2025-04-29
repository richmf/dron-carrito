from flask import Flask

app = Flask(__name__) #iniciamos una aplicacion con flask

#creamos algunas rutas para diversas funciones
@app.route("/")#pagina inical
def index():
    return "Hello from Flask"
@app.route("/push-button")#convencion de separacion en ULS
def check_push_button_state():
    return "ok"
app.run(host="0.0.0.0")