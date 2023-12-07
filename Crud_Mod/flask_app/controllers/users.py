from flask import Flask, render_template, request, redirect
from flask_app.models.users import User
from flask_app import app


@app.route('/')
def index():
    users = User.muestra_usuarios()
    return render_template("index.html",users=users) 

@app.route('/new')
def new():
    return render_template("new.html")

@app.route('/create', methods=['POST'])
def create():
    print(request.form)
    User.guardar(request.form)
    return redirect('/')

@app.route('/delete/<id>', methods=['GET', 'DELETE'])
def delete(id):
    data = {
        "id": id
    }
    User.borrar(data)
    return redirect('/')


@app.route('/edit/<int:id>')
def edit(id):
    data = {
        "id": id
    }
    user = User.mostrar(data)
    return render_template('edit.html', user=user)

@app.route('/update', methods = ['POST'])
def update():
    form_data = request.form
    print(form_data)
    User.actualizar(request.form)
    return redirect('/')

