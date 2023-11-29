from flask import Flask, render_template #importamos flask para permitirnos crear la aplicacion

app = Flask(__name__)#Creando una instancia de Flask y la llamo app

@app.route('/') #en la ruta / me va a ejecutar la función que vaya en la siguiente linea
def hola_mundo():
  return "Hola mundo!" #al acceder a mi ruta '/' me regresa un Hola mundo!

@app.route('/hola/<nombre>')
def hola_nombre(nombre):
  return "Hola "+nombre

@app.route('/hello')
def hola_mundo2():
  #En lugar de devolver una cadena/texto
  #Devolviendo el resultado del metodo render_template, pasando el nombre de mi archivo HTML
  return render_template('index.html', nombre="John") #JINJA

if __name__ == '__main__': #Asegurandose de que el archivo se ejecute directamente y NO desde otro modulo
  app.run(debug=True) #Ejecute mi aplicación
