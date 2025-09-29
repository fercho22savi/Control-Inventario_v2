
# administrador.py
<<<<<<< HEAD
class AdministradorUsuarios:
    def __init__(self):
        self.usuarios = {"admin": "admin_pass"}  # Usuario admin por defecto

    def registrar_usuario(self, username, password):
=======
class AdministradorUsuarios:# Clase para gestionar usuarios
    def __init__(self):
        self.usuarios = {"admin": "admin_pass"}  

    def registrar_usuario(self, username, password):# Método para registrar un nuevo usuario
>>>>>>> db887b8 (Actualizando interfaces de usuario colores y funciones)
        if username in self.usuarios:
            return False  # El usuario ya existe
        else:
            self.usuarios[username] = password
            return True  # Registro exitoso

<<<<<<< HEAD
    def autenticar_usuario(self, username, password):
=======
    def autenticar_usuario(self, username, password):# Método para autenticar un usuario
>>>>>>> db887b8 (Actualizando interfaces de usuario colores y funciones)
        if username not in self.usuarios:
            return None  # Usuario no registrado
        return self.usuarios.get(username) == password
