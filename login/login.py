<<<<<<< HEAD
import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageDraw
import os
from modules.dashboard import Dashboard  

class LoginModerno(ctk.CTk):
    def __init__(self, master):
        self.master = master
        super().__init__()

        # Configuración de ventana
        self.title("Login")
        self.geometry("450x500")
        self.resizable(False, False)
        self.configure(bg="black")
        self.wm_attributes("-alpha", 0.85)
        self.LoginModerno = {}
        self.current_user = None # Variable para almacenar el usuario actual

        # Estilo general
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        # --------- Cargar LOGO (o crear uno temporal) ---------
        logo_path = "logo.png"
        if not os.path.exists(logo_path):
            img = Image.new("RGBA", (100, 100), (30, 30, 30, 255))  # Fondo oscuro
            draw = ImageDraw.Draw(img)
            draw.text((25, 40), "LOGO", fill="white")
=======
import sys
import tkinter as tk
import customtkinter as ctk
import os
from tkinter import messagebox
from PIL import Image, ImageDraw
import sys, os
# añade la carpeta raíz (Login_Python) al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
#from dashboard import Dashboard
from registro import DummyAdminUsuarios, RegistroApp


PALETA = {
    "fondo": "#121B2E",
    "panel": "#104E8B",
    "texto": "#E6E6E6",
    "texto_secundario": "#7A8BA3",
    "resaltado": "#00BFFF",
    "boton": "#1E90FF",
    "peligro": "#B22222",
    "peligro_hover": "#FF4040"
}


# Clase principal de la aplicación de login
class LoginModerno(ctk.CTk):  
    def __init__(self):
        super().__init__() 
        # Configuración de la ventana principal
        self.title("Login")
        # Tamaño fijo de la ventana
        self.geometry("450x500")
        # Deshabilitar el redimensionamiento
        self.resizable(False, False)
        # Configuración de colores y transparencia
        self.configure(fg_color=PALETA["fondo"])
        self.wm_attributes("-alpha", 0.85)
        # Variable para almacenar el usuario actual
        self.current_user = None

        # Configuración de apariencia
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        # Logo
        logo_path = os.path.join(os.path.dirname(__file__), "cuenta.png")  # Ruta del logo
        if not os.path.exists(logo_path):
            img = Image.new("RGBA", (100, 100), (30, 30, 30, 255))
            draw = ImageDraw.Draw(img)
            draw.text((25, 40), "LOGO", fill="white")
            img.save(logo_path)  # Guardar el logo generado
>>>>>>> db887b8 (Actualizando interfaces de usuario colores y funciones)
        else:
            img = Image.open(logo_path)

        logo_img = ctk.CTkImage(light_image=img, size=(100, 100))
        self.logo = ctk.CTkLabel(self, image=logo_img, text="")
        self.logo.pack(pady=20)

<<<<<<< HEAD
        # --------- Título ---------
        self.label_title = ctk.CTkLabel(self, text="Bienvenido", font=("Arial", 24, "bold"))
        self.label_title.pack(pady=10)

        # --------- Campo Usuario ---------
        self.username_label = ctk.CTkLabel(self, text="Usuario")
        self.username_label.pack(pady=5)
        self.username_entry = ctk.CTkEntry(self, placeholder_text="Ingresa tu usuario")
        self.username_entry.pack(pady=5)

        # --------- Campo Contraseña ---------
        self.password_label = ctk.CTkLabel(self, text="Contraseña")
        self.password_label.pack(pady=5)
        self.password_entry = ctk.CTkEntry(self, placeholder_text="Ingresa tu contraseña", show="*")
        self.password_entry.pack(pady=5)

        # --------- Checkbox Recordar ---------
=======
        # Etiqueta de bienvenida
        ctk.CTkLabel(self, text="Bienvenido", font=("Arial", 24, "bold")).pack(pady=10)

        # Campo de usuario
        ctk.CTkLabel(self, text="Usuario").pack(pady=5)
        self.username_entry = ctk.CTkEntry(self, placeholder_text="Ingresa tu usuario")
        self.username_entry.pack(pady=5)

        # Campo de contraseña
        ctk.CTkLabel(self, text="Contraseña").pack(pady=5)
        self.password_entry = ctk.CTkEntry(self, placeholder_text="Ingresa tu contraseña", show="*")
        self.password_entry.pack(pady=5)

        # Checkbox para recordar contraseña
>>>>>>> db887b8 (Actualizando interfaces de usuario colores y funciones)
        self.remember_var = tk.BooleanVar()
        self.remember_check = ctk.CTkCheckBox(self, text="Recordar contraseña", variable=self.remember_var)
        self.remember_check.pack(pady=10)

<<<<<<< HEAD
        # --------- Botón Ingresar ---------
        self.login_button = ctk.CTkButton(self, text="Ingresar", command=self.login)
        self.login_button.pack(pady=10)

        # --------- Botón Registrarse ---------
        self.register_button = ctk.CTkButton(self, text="Registrarse", command=self.registrarse)
        self.register_button.pack(pady=5)

    # --------- Lógica de ingreso con validaciones ---------
    def login(self):
=======
        # Botón de login
        self.login_button = ctk.CTkButton(self, text="Ingresar", command=self.login)
        self.login_button.pack(pady=10)
        

        # Botón de registro
        self.register_button = ctk.CTkButton(self, text="Registrarse", command=self.registrarse, fg_color=PALETA["resaltado"], hover_color="#1E90FF")
        self.register_button.pack(pady=5)

    # Definición de métodos para manejar eventos de la interfaz gráfica
    def login(self):
        """Lógica para manejar el inicio de sesión."""
>>>>>>> db887b8 (Actualizando interfaces de usuario colores y funciones)
        usuario = self.username_entry.get().strip()
        contrasena = self.password_entry.get().strip()

        if not usuario or not contrasena:
            messagebox.showwarning("Campos Vacíos", "Por favor, completa todos los campos.")
            return

<<<<<<< HEAD
        # validación de usuario y contraseña
        if usuario == "admin" and contrasena == "admin":
=======
        # Usuarios válidos (esto debería reemplazarse con una base de datos en producción)
        valid_users = {
            "admin": "admin123",
            "miembro": "password1",
            "invitado": "password2"
        }
        if usuario in valid_users and valid_users[usuario] == contrasena:
>>>>>>> db887b8 (Actualizando interfaces de usuario colores y funciones)
            messagebox.showinfo("Login Exitoso", f"¡Bienvenido {usuario}!")
            self.current_user = usuario
            if self.remember_var.get():
                print(f"Recordar credenciales para: {usuario}")
<<<<<<< HEAD
            self.to_dashboard()  # Cambiar a la función to_dashboard
        else:
            messagebox.showerror("Error de Acceso", "Usuario o contraseña incorrectos.")

    def registrarse(self):
        messagebox.showinfo("Registro", "Aquí se abriría la ventana de registro.")
    

    def to_dashboard(self):
        self.destroy()
        self.master.deiconify()


# --------- Ejecución directa ---------
=======
            self.to_dashboard()
        else:
            messagebox.showerror("Error de Acceso", "Usuario o contraseña incorrectos.")
            # metodo para conectar login con dashboard
def to_dashboard(self):
    """Método para abrir el dashboard después de un login exitoso."""
    self.destroy()
    dashboard = Dashboard(usuario=self.current_user)  # si Dashboard acepta el usuario
    dashboard.mainloop()

def registrarse(self):  # Método para manejar el registro de nuevos usuarios
    """Lógica para manejar el registro."""
    self.destroy()  # Cerrar la ventana actual antes de abrir la de registro
    registro = RegistroApp(admin_usuarios=DummyAdminUsuarios())
    registro.mainloop()

   

>>>>>>> db887b8 (Actualizando interfaces de usuario colores y funciones)
if __name__ == "__main__":
    app = LoginModerno()
    app.mainloop()
