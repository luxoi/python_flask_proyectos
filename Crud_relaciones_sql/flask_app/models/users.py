from flask_app.config.mysqlconnector import connectToMySQL
from .classrooms import Classroom

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.classrooms_id = data['classrooms_id']
        self.classroom = None

    @classmethod
    @classmethod
    def muestra_usuarios(cls):
        query = "SELECT * FROM users"
        results = connectToMySQL('esquema_usuarios').query_db(query)
        users = []
        for u in results:
            usr = cls(u)
            data = {
                "id": usr.classrooms_id
            }
            classr = Classroom.muestra_salon(data)
            usr.classroom = classr  
            users.append(usr)  # Aquí está el cambio
        return users   


    @classmethod
    def guardar(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, classrooms_id) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(classrooms_id)s)"
        result = connectToMySQL('esquema_usuarios').query_db(query, data)
        return result

    

    @classmethod
    def borrar(cls, formulario):
        query = "DELETE FROM users WHERE id = %(id)s"
        result = connectToMySQL('esquema_usuarios').query_db(query, formulario)
        return result

    @classmethod
    def mostrar(cls, formulario):
        query = "SELECT * FROM users WHERE id = %(id)s"
        result = connectToMySQL('esquema_usuarios').query_db(query, formulario)    
        user = result[0]
        user = cls(user)
        return user


    @classmethod
    def actualizar(cls, formulario):
        #formulario = {"id": "1", "first_name": "C", "last_name": "X", "email": "c@cd.com"}
        query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s, %(classrooms_id)s WHERE id=%(id)s"
        result = connectToMySQL('esquema_usuarios').query_db(query, formulario)
        return result