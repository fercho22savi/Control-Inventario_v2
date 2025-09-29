import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageDraw
import os




class LoginModerno(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configuración de ventana
        self.title("Login")
        self.geometry("450x500")
        self.resizable(False, False)
        self.configure(bg="black")
        self.wm_attributes("-alpha", 0.85)
        self.current_user = None

        # Estilo general
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        # --------- Cargar LOGO ---------
        logo_path = "logo.png"
        if not os.path.exists(logo_path):
            img = Image.new("RGBA", (100, 100), (30, 30, 30, 255))
            draw = ImageDraw.Draw(img)
            draw.text((25, 40), "LOGO", fill="white")
        else:
            img = Image.open(logo_path)

        logo_img = ctk.CTkImage(light_image=img, size=(100, 100))
        self.logo = ctk.CTkLabel(self, image=logo_img, text="")
        self.logo.pack(pady=20)

        # --------- Título ---------
        ctk.CTkLabel(self, text="Bienvenido", font=("Arial", 24, "bold")).pack(pady=10)

        # --------- Usuario ---------
        ctk.CTkLabel(self, text="Usuario").pack(pady=5)
        self.username_entry = ctk.CTkEntry(self, placeholder_text="Ingresa tu usuario")
        self.username_entry.pack(pady=5)

        # --------- Contraseña ---------
        ctk.CTkLabel(self, text="Contraseña").pack(pady=5)
        self.password_entry = ctk.CTkEntry(self, placeholder_text="Ingresa tu contraseña", show="*")
        self.password_entry.pack(pady=5)

        # --------- Recordar ---------
        self.remember_var = ctk.BooleanVar()
        ctk.CTkCheckBox(self, text="Recordar contraseña", variable=self.remember_var).pack(pady=10)

        # --------- Botones ---------
        ctk.CTkButton(self, text="Ingresar", command=self.login).pack(pady=10)
        ctk.CTkButton(self, text="Registrarse", command=self.registrarse).pack(pady=5)

    def login(self):
        usuario = self.username_entry.get().strip()
        contrasena = self.password_entry.get().strip()

        if not usuario or not contrasena:
            messagebox.showwarning("Campos Vacíos", "Por favor, completa todos los campos.")
            return

        valid_users = {
            "admin": "admin123",
            "miembro": "password1",
            "invitado": "password2"
        }
        if usuario in valid_users and valid_users[usuario] == contrasena:
            messagebox.showinfo("Login Exitoso", f"¡Bienvenido {usuario}!")
            self.current_user = usuario
            self.to_dashboard()
        else:
            messagebox.showerror("Error de Acceso", "Usuario o contraseña incorrectos.")

    def registrarse(self):
        messagebox.showinfo("Registro", "Aquí se abriría la ventana de registro.")

    def to_dashboard(self):
        self.destroy()
        dashboard = Dashboard()   # 👈 abrir dashboard
        dashboard.mainloop()


if __name__ == "__main__":
    app = LoginModerno()
    app.mainloop()
