from mysqlconnection import connectToMySQL

class Usuario:
    def __init__(self, datos):
                self.id = datos.get("id")
                self.nombre = datos.get("nombre")
                self.apellido = datos.get("apellido")
                self.email = datos.get("email")
                self.created_at = datos.get("created_at")
                self.updated_at = datos.get("updated_at")

    @classmethod
    def save(cls, datos):
        query = "INSERT INTO usuarios (nombre, apellido, email, updated_at, created_at) VALUES(%(nombre)s, %(apellido)s, %(email)s, NOW(), NOW());"
        return connectToMySQL('usuarios_crud').query_db(query, datos)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios;"
        usuarios_bd = connectToMySQL('usuarios_crud').query_db(query)
        usuarios = []
        for usuario in usuarios_bd:
            usuarios.append(cls(usuario))
        return usuarios
    
    @classmethod
    def get_one(cls,datos):
        query = "SELECT * FROM usuarios WHERE id = %(id)s;"
        usuarios_bd = connectToMySQL('usuarios_crud').query_db(query,datos)

        return cls(usuarios_bd[0])
    
    @classmethod
    def update(cls, datos):
        query = "UPDATE usuarios SET nombre=%(nombre)s, apellido=%(apellido)s, email=%(email)s WHERE id = %(id)s;"
        return connectToMySQL('usuarios_crud').query_db(query, datos)
    
    @classmethod
    def delete(cls, datos):
        query = "DELETE FROM usuarios WHERE id = %(id)s;"
        return connectToMySQL('usuarios_crud').query_db(query, datos)



