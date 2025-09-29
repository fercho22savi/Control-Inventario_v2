# main.py
import tkinter as tk
import customtkinter as ctk

from login import LoginApp
<<<<<<< HEAD
from modules.administrador import AdministradorUsuarios

if __name__ == "__main__":
    admin_usuarios = AdministradorUsuarios()  # Instancia del Administrador de Usuarios
    app = LoginApp(admin_usuarios)  # Pasamos el administrador de usuarios a la app
    app.mainloop()




=======
from modules.UserActivityDashboard import UserActivityDashboard
from modules.dashboard import Dashboard
from modules.user_Info import UserProfile, UserProfileWindow
from login.login import LoginModerno


if __name__ == "__main__":
    admin_usuarios = UserActivityDashboard()  # Instancia del Administrador de Usuarios
    app = LoginModerno(admin_usuarios)  # Pasamos el administrador de usuarios a la app
    app.mainloop()

>>>>>>> db887b8 (Actualizando interfaces de usuario colores y funciones)
