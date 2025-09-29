import customtkinter as ct
from tkinter import messagebox
# Importar la biblioteca re para expresiones regulares
import re 

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

# Clase  para manejo  con tipo usuarios
class DummyAdminUsuarios:
    def __init__(self):
        self.usuarios = {}
    # Función para registrar usuario
    def registrar_usuario(self, username, password, tipo_usuario):
        if username in self.usuarios:
            return False
        self.usuarios[username] = {
            "password": password,
            "tipo": tipo_usuario
        }
        print(f"Usuario '{username}' registrado con éxito como '{tipo_usuario}'.")
        return True

# class RegistroApp
class RegistroApp(ct.CTk):
    def __init__(self, admin_usuarios):
        super().__init__()
        self.admin_usuarios = admin_usuarios

        # Estilo
        ct.set_appearance_mode("dark")
        ct.set_default_color_theme("dark-blue")

        # Ventana
        self.title("Registro de Usuario")
        self.geometry("500x600")
        self.resizable(False, False)
        self.configure(fg_color=PALETA["fondo"])
        self.wm_attributes("-alpha", 0.85)

        fuente = ("Arial", 14)

        ct.CTkLabel(self, text="Crear Cuenta", font=("Arial", 22, "bold"), text_color=PALETA["resaltado"]).pack(pady=20)

        # Tipo de usuario
        ct.CTkLabel(self, text="Tipo de Usuario:", font=fuente, text_color=PALETA["texto"]).pack(pady=(10, 2))
        self.user_type_var = ct.StringVar(value="user")  # Valor por defecto
        self.user_type_menu = ct.CTkOptionMenu(
            self,
            values=["user", "admin"],     # Opciones del menú
            variable=self.user_type_var,  # Valor por defecto
            width=250,                    # Ancho del menú
            font=fuente,                  # Fuente del menú
            fg_color=PALETA["texto_secundario"],# Mismo fondo que el formulario
            button_color=PALETA["boton"],       # Igual que el botón de registro
            button_hover_color="#21867A", # Color al pasar el mouse
            text_color="white"            # Color del texto
        )
        self.user_type_menu.pack()

        # Nombre completo (opcional)
        ct.CTkLabel(self, text="Nombre Completo (opcional):", font=fuente).pack(pady=(10, 2))
        self.fullname_entry = ct.CTkEntry(self, width=250, font=fuente, placeholder_text="Ingrese su nombre completo")
        self.fullname_entry.pack()
        
        # Edad (opcional)
        ct.CTkLabel(self, text="Edad (opcional):", font=fuente).pack(pady=(10, 2))
        self.age_entry = ct.CTkEntry(self, width=250, font=fuente, placeholder_text="Ingrese su edad")
        self.age_entry.pack()

        # Usuario
        ct.CTkLabel(self, text="Usuario:", font=fuente).pack(pady=(10, 2))
        self.username_entry = ct.CTkEntry(self, width=250, font=fuente, placeholder_text="Ingrese su usuario")
        self.username_entry.pack()

        # Contraseña
        ct.CTkLabel(self, text="Contraseña:", font=fuente).pack(pady=(10, 2))
        self.password_entry = ct.CTkEntry(self, show="*", width=250, font=fuente, placeholder_text="Ingrese su contraseña")
        self.password_entry.pack()

        # Confirmar contraseña
        ct.CTkLabel(self, text="Confirmar Contraseña:", font=fuente).pack(pady=(10, 2))
        self.confirm_password_entry = ct.CTkEntry(self, show="*", width=250, font=fuente, placeholder_text="Repita la contraseña")
        self.confirm_password_entry.pack()
             
        # Botón de registro
        ct.CTkButton(self, text="Registrar", font=fuente,
                     fg_color=PALETA["boton"], command=self.register_user).pack(pady=25)
        


        self.after(100, lambda: self.username_entry.focus())

    # registrar_usuario
    def register_user(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        confirm_password = self.confirm_password_entry.get().strip()
        tipo_usuario = self.user_type_var.get()

        # Validaciones
        if not username or not password or not confirm_password:
            messagebox.showwarning("Campos vacíos", "Por favor, complete todos los campos.")
            return
        
        # Validar que el nombre de usuario no esté vacío
        if len(username) < 4:
            messagebox.showwarning("Usuario inválido", "El nombre de usuario debe tener al menos 4 caracteres.")
            return

        # Validar que el nombre de usuario no contenga caracteres especiales
        if not re.match(r"^[a-zA-Z0-9_]+$", username):
            messagebox.showwarning("Usuario inválido", "El usuario solo puede contener letras, números y guiones bajos.")
            return

        # Validar la contraseña
        if len(password) < 6:
            messagebox.showwarning("Contraseña inválida", "La contraseña debe tener al menos 6 caracteres.")
            return
        # Validar que las contraseñas no coincidan
        if password != confirm_password:
            messagebox.showerror("Registro fallido", "Las contraseñas no coinciden.")
            return

        # Validar existencia del administrador
        if not self.admin_usuarios:
            messagebox.showerror("Registro fallido", "No se puede registrar sin un administrador.")
            return

        # Registrar el usuario
        if self.admin_usuarios.registrar_usuario(username, password, tipo_usuario):
            messagebox.showinfo("Éxito", f"¡Usuario '{username}' registrado correctamente como '{tipo_usuario}'!")
            self.destroy()
        else:
            messagebox.showerror("Registro fallido", "¡El nombre de usuario ya existe!")
            self.username_entry.delete(0, 'end')
            self.password_entry.delete(0, 'end')
            self.confirm_password_entry.delete(0, 'end')


if __name__ == "__main__":
    app = RegistroApp(admin_usuarios=DummyAdminUsuarios())
    app.mainloop()
