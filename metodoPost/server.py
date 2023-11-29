from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = "llave super secreta" #Establecemos una clave secreta para dar mas seguridad a las cookies

#En nuestra ruta raiz quiero que se meustre un formulario
@app.route("/")
def formulario():
    return render_template("index.html")

#Ponemos action a nuestro formulario
@app.route("/success", methods=['POST'])
def crearUser():
  print(request.form)

  #Guardamos info en sesión
  session['usuario'] = request.form['nombre']
  session['email'] = request.form['email']

  #Usamos redirect para evitar el reenvio del formulario
  return redirect('procesado')

@app.route("/procesado")
def procesado():
  return render_template("procesado.html")

if __name__ == '__main__': #Asegurandose de que el archivo se ejecute directamente y NO desde otro modulo
  app.run(debug=True)
