from flask import Flask, render_template, request, redirect
from mysqlconecction import connectToMySQL

app = Flask(__name__)

@app.route('/')
def index():
    query = "SELECT * FROM usuarios"
    result = connectToMySQL('registrologin').query_db(query)
    return render_template('/index.html', result=result)

@app.route('/insert')
def insert():

    data = {
        "nombre": "pedro",
        "apellido": "piedra",
        "id": "6"
    }

    query = "INSERT INTO usuarios (nombre, apellido, id) VALUES (%(nombre)s, %(apellido)s, %(id)s)"
    result = connectToMySQL('registrologin').query_db(query, data)
    return render_template('/insert.html')


@app.route('/delete/<id>')
def delete(id):
    data = {
        "id": id
    }

    query = "DELETE FROM usuarios WHERE id = %(id)s"
    result = connectToMySQL('registrologin').query_db(query, data)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True) 