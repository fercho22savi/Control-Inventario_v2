import customtkinter as ct
from datetime import datetime
from dashboard import Dashboard
from tkinter import filedialog
import os
import sqlite3
from dashboard import Dashboard


# ---------------------------
# Paleta de colores estilo dashboard
# ---------------------------
PALETA = {
    "fondo": "#0A0F1C",
    "panel": "#121B2E",
    "texto": "#E6E6E6",
    "texto_secundario": "#7A8BA3",
    "resaltado": "#00BFFF",
    "boton": "#1E90FF",
    "peligro": "#B22222",
    "peligro_hover": "#FF4040"
}


# ---------------------------
# Modelo de perfil de usuario
# ---------------------------
class UserProfile:
    def __init__(self, username, email, full_name=None, age=None, role="Usuario", last_login=None, avatar_path=None):
        self.username = username
        self.email = email
        self.full_name = full_name
        self.age = age
        self.role = role
        self.is_active = True
        self.last_login = last_login or datetime.now().strftime("%d/%m/%Y %H:%M")
        self.avatar_path = avatar_path or "avatars/default.png"

        # Crear carpeta de avatares si no existe
        if not os.path.exists("avatars"):
            os.makedirs("avatars")
    # Actualizar perfil
    def update_profile(self, full_name=None, age=None, email=None, avatar_path=None):
        if full_name is not None:
            self.full_name = full_name
        if age is not None:
            self.age = age
        if email is not None:
            self.email = email
        if avatar_path is not None:
            self.avatar_path = avatar_path

        # Guardar en la BD (ejemplo SQLite)
        conn = sqlite3.connect("usuarios.db")
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                username TEXT PRIMARY KEY,
                email TEXT,
                full_name TEXT,
                age INTEGER,
                role TEXT,
                is_active INTEGER,
                last_login TEXT,
                avatar_path TEXT
            )
        """)
        c.execute("""
            INSERT OR REPLACE INTO usuarios (username, email, full_name, age, role, is_active, last_login, avatar_path)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (self.username, self.email, self.full_name, self.age, self.role,
              int(self.is_active), self.last_login, self.avatar_path))
        conn.commit()
        conn.close()
    # Cambiar contraseña
    def change_password(self, new_password):
        self.last_login = datetime.now().strftime("%d/%m/%Y %H:%M")
        self.update_profile()  
        
        # Aquí podrías guardar en BD la contraseña (ideal con hash)
        print(f"Contraseña cambiada a: {new_password}" )


# ----------------------------
# Ventana de perfil de usuario
# ----------------------------
class UserProfileWindow(ct.CTk):
    def __init__(self, user_profile: UserProfile):
        super().__init__()
        self.user_profile = user_profile

        # Configuración ventana
        self.title("Perfil de Usuario")
        self.geometry("420x620")
        self.resizable(False, False)
        self.configure(fg_color=PALETA["fondo"])
        self.wm_attributes("-alpha", 0.85)

        # Mantener al frente
        self.lift()
        self.focus_force()

        # Título
        ct.CTkLabel(
            self, text="Perfil de Usuario",
            font=("Arial", 22, "bold"),
            text_color=PALETA["resaltado"]
        ).pack(pady=15)

        # Avatar
        self.avatar_label = ct.CTkLabel(self, text="")
        self.avatar_label.pack(pady=10)
        self.cargar_avatar()

        ct.CTkButton(
            self, text="📷 Cambiar Avatar",
            fg_color=PALETA["boton"], hover_color=PALETA["resaltado"],
            text_color="white", command=self.cambiar_avatar
        ).pack(pady=5)

        # Info
        self.info_labels = {}
        self.update_info_display()

        # Botones
        botones_frame = ct.CTkFrame(self, fg_color=PALETA["panel"])
        botones_frame.pack(pady=20)
        # Boton editar perfil
        ct.CTkButton(
            botones_frame, text="✏️ Editar Perfil", width=150,
            fg_color=PALETA["boton"], hover_color=PALETA["resaltado"],
            text_color="white", command=self.editar_perfil
        ).grid(row=0, column=0, padx=10, pady=5)
        # Boton cambiar contraseña
        ct.CTkButton(
            botones_frame, text="Cambiar Contraseña", width=180,
            fg_color=PALETA["boton"], hover_color=PALETA["resaltado"],
            text_color="white", command=self.cambiar_contrasena
        ).grid(row=0, column=1, padx=10, pady=5)
        # Boton cerrar
        ct.CTkButton(
            botones_frame, text="Cerrar", width=150,
            fg_color=PALETA["peligro"], hover_color=PALETA["peligro_hover"],
            text_color="white", command=self.destroy
        ).grid(row=1, column=0, padx=10, pady=10)
        # Boton regresar
        ct.CTkButton(
            botones_frame, text="Regresar", width=180,
            fg_color=PALETA["boton"], hover_color=PALETA["resaltado"],
            text_color="white", command=self.regresar_dashboard
        ).grid(row=1, column=1, padx=10, pady=10)
    # Cargar avatar
    def cargar_avatar(self):
        if os.path.exists(self.user_profile.avatar_path):
            img = ct.CTkImage(dark_image=None, light_image=None, size=(100, 100))
            self.avatar_label.configure(image=img, text="")
            self.avatar_label.image = img
        else:
            self.avatar_label.configure(text="🧑", font=("Arial", 65), text_color=PALETA["texto"])
    # Cambiar avatar
    def cambiar_avatar(self):
        ruta = filedialog.askopenfilename(
            title="Seleccionar imagen",
            filetypes=[("Archivos de imagen", "*.png;*.jpg;*.jpeg;*.gif")]
        )
        if ruta:
            # Guardar copia en carpeta avatars
            destino = os.path.join("avatars", os.path.basename(ruta))
            with open(ruta, "rb") as f_in, open(destino, "wb") as f_out:
                f_out.write(f_in.read())

            self.user_profile.update_profile(avatar_path=destino)
            self.cargar_avatar()
    # Actualizar display de info
    def update_info_display(self):
        for lbl in self.info_labels.values():
            lbl.destroy()

        info = {
            "Usuario": self.user_profile.username,
            "Email": self.user_profile.email,
            "Nombre": self.user_profile.full_name or "N/A",
            "Rol": self.user_profile.role,
            "Edad": self.user_profile.age or "N/A",
            "Estado": "Activo" if self.user_profile.is_active else "Inactivo",
            "Último acceso": self.user_profile.last_login
        }

        for key, value in info.items():
            self.info_labels[key] = ct.CTkLabel(
                self, text=f"{key}: {value}",
                font=("Arial", 14), text_color=PALETA["texto"]
            )
            self.info_labels[key].pack(pady=3)

    # Editar perfil
    def editar_perfil(self):
        win = ct.CTkToplevel(self)
        win.title("Editar Perfil")
        win.geometry("350x350")
        win.configure(fg_color=PALETA["panel"])

        ct.CTkLabel(win, text="Nombre completo:", text_color=PALETA["texto"]).pack(pady=5)
        entry_nombre = ct.CTkEntry(win, width=250)
        entry_nombre.insert(0, self.user_profile.full_name or "")
        entry_nombre.pack(pady=5)

        ct.CTkLabel(win, text="Edad:", text_color=PALETA["texto"]).pack(pady=5)
        entry_edad = ct.CTkEntry(win, width=250)
        entry_edad.insert(0, str(self.user_profile.age or ""))
        entry_edad.pack(pady=5)

        ct.CTkLabel(win, text="Email:", text_color=PALETA["texto"]).pack(pady=5)
        entry_email = ct.CTkEntry(win, width=250)
        entry_email.insert(0, self.user_profile.email)
        entry_email.pack(pady=5)
        # Guardar cambios
        def guardar():
            self.user_profile.update_profile(
                full_name=entry_nombre.get(),
                age=int(entry_edad.get()) if entry_edad.get().isdigit() else None,
                email=entry_email.get()
            )
            self.update_info_display()
            win.destroy()
        
        ct.CTkButton(
            win, text="Guardar",
            fg_color=PALETA["boton"], hover_color=PALETA["resaltado"],
            text_color="white", command=guardar
        ).pack(pady=20)

    # Cambiar contraseña
    def cambiar_contrasena(self):
        win = ct.CTkToplevel(self)
        win.title("Cambiar Contraseña")
        win.geometry("350x250")
        win.configure(fg_color=PALETA["panel"])

        ct.CTkLabel(win, text="Nueva Contraseña:", text_color=PALETA["texto"]).pack(pady=10)
        entry_pass = ct.CTkEntry(win, show="*", width=250)
        entry_pass.pack(pady=5)

        ct.CTkLabel(win, text="Confirmar Contraseña:", text_color=PALETA["texto"]).pack(pady=10)
        entry_confirm = ct.CTkEntry(win, show="*", width=250)
        entry_confirm.pack(pady=5)
        # Guardar nueva contraseña
        def guardar():
            if entry_pass.get() == entry_confirm.get() and entry_pass.get() != "":
                self.user_profile.change_password(entry_pass.get())
                win.destroy()
            else:
                ct.CTkLabel(win, text="Las contraseñas no coinciden", text_color="red").pack(pady=10)

        ct.CTkButton(
            win, text="Guardar",
            fg_color=PALETA["boton"], hover_color=PALETA["resaltado"],
            text_color="white", command=guardar
        ).pack(pady=20)
    # Regresar al dashboard
    def regresar_dashboard(self):
        self.destroy()
        dash = Dashboard()
        dash.mainloop()
            


# ----------------------------
# Ejemplo de ejecución
# ----------------------------
if __name__ == "__main__":
    usuario = UserProfile("admin", "admin@correo.com", "Administrador General", 30, role="SuperAdmin")
    app = UserProfileWindow(usuario)
    app.mainloop()
