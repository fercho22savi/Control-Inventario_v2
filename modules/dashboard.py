# -*- coding: utf-8 -*-
<<<<<<< HEAD
# Este módulo es parte de un sistema de gestión de clientes y proveedores.
# Su propósito es proporcionar un panel de control para acceder a diferentes módulos de la aplicación.
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import customtkinter as ct
from clients import ClientsApp
from modules.suppliers import SuppliersApp
from modules.products import ProductApp


class Dashboard(ct.CTk):# Clase principal del Dashboard
    def __init__(self):
        super().__init__()
        self.title("Dashboard")
        self.geometry("800x500")
        self.resizable(False, False)
        self.configure(fg_color="black")
        self.wm_attributes("-alpha", 0.95)

        ct.CTkLabel(self, text="MODULOS", font=("Helvetica", 22, "bold"), text_color="white").pack(pady=40)

        ct.CTkButton(self,
                     text="Módulo Proveedores",
                     font=("Helvetica", 14),
                     width=240,
                     fg_color="#2A9D8F",
                     hover_color="#21867A",
                     text_color="white",
                     command=self.open_suppliers_module).pack(pady=20)

        ct.CTkButton(self,
                     text="Módulo Clientes",
                     font=("Helvetica", 14),
                     width=240,
                     fg_color="#2A9D8F",
                     hover_color="#21867A",
                     text_color="white",
                     command=self.open_clients_module).pack(pady=20)

        ct.CTkButton(self,
                     text="Módulo Productos",
                     font=("Helvetica", 14),
                     width=240,
                     fg_color="#2A9D8F",
                     hover_color="#21867A",
                     text_color="white",
                     command=self.open_products_module).pack(pady=20)

        ct.CTkButton(self,
                     text="Salir",
                     font=("Helvetica", 14),
                     width=240,
                     fg_color="#E76F51",
                     hover_color="#D35445",
                     text_color="white",
                     command=self.quit).pack(pady=10)

    def open_suppliers_module(self):# Método para abrir el módulo de proveedores
=======
# Dashboard principal del sistema

import customtkinter as ct  # Importar la biblioteca customtkinter
from clients import ClientsApp
from suppliers import SuppliersApp
from products import ProductApp
from UserActivityDashboard import UserActivityDashboard

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


class Dashboard(ct.CTk):  # Clase principal del Dashboard
    def __init__(self):
        super().__init__()
        
        # Configuración de la ventana principal del Dashboard
        self.title("Dashboard")
        self.geometry("800x600")
        self.resizable(False, False)
        self.configure(fg_color=PALETA["fondo"])
        self.wm_attributes("-alpha", 0.85)

        # Título
        ct.CTkLabel(
            self,
            text="MÓDULOS",
            font=("Helvetica", 22, "bold"),
            text_color=PALETA["resaltado"]
        ).pack(pady=40)

        # Configuración base para los botones
        button_style = {
            "font": ("Helvetica", 14, "bold"),
            "width": 240,
            "fg_color": PALETA["boton"],
            "text_color": PALETA["texto"],
            "corner_radius": 12,
            "height": 40
        }

        # Botones principales
        ct.CTkButton(self, text="Módulo Proveedores",
                     command=self.open_suppliers_module, **button_style).pack(pady=15)

        ct.CTkButton(self, text="Módulo Clientes",
                     command=self.open_clients_module, **button_style).pack(pady=15)

        ct.CTkButton(self, text="Módulo Productos",
                     command=self.open_products_module, **button_style).pack(pady=15)

        ct.CTkButton(self, text="Administrar Usuarios",
                     command=self.open_user_activity_module, **button_style).pack(pady=15)

        ct.CTkButton(self, text="Ver Perfil",
                     command=self.view_profile, **button_style).pack(pady=15)

        # Botón de cierre con colores de peligro
        ct.CTkButton(
            self,
            text="Cerrar Sesión",
            font=("Helvetica", 14, "bold"),
            width=240,
            fg_color=PALETA["peligro"],
            hover_color=PALETA["peligro_hover"],
            text_color="white",
            corner_radius=12,
            height=40,
            command=self.destroy
        ).pack(pady=20)

    # Métodos módulo proveedores
    def open_suppliers_module(self):
>>>>>>> db887b8 (Actualizando interfaces de usuario colores y funciones)
        print("Abriendo módulo de proveedores...")
        self.withdraw()
        app = SuppliersApp(self)
        app.mainloop()
        self.deiconify()
<<<<<<< HEAD

    def open_clients_module(self):# Método para abrir el módulo de clientes
=======
    # Método módulo clientes
    def open_clients_module(self):
>>>>>>> db887b8 (Actualizando interfaces de usuario colores y funciones)
        print("Abriendo módulo de clientes...")
        self.withdraw()
        app = ClientsApp(self)
        app.mainloop()
        self.deiconify()
<<<<<<< HEAD

    def open_products_module(self):# Método para abrir el módulo de productos
=======
    # Método módulo productos
    def open_products_module(self):
>>>>>>> db887b8 (Actualizando interfaces de usuario colores y funciones)
        print("Abriendo módulo de productos...")
        self.withdraw()
        app = ProductApp(self)
        app.mainloop()
        self.deiconify()
<<<<<<< HEAD

    def back_to_dashboard(self):# Método para regresar al dashboard
        print("Regresando al Dashboard...")
        self.destroy()
        dashboard = Dashboard()
        dashboard.mainloop()


if __name__ == "__main__":
    print("Iniciando Dashboard...")
=======
    # Método módulo actividad de usuarios
    def open_user_activity_module(self):
        print("Abriendo módulo de actividad de usuarios...")
        self.withdraw()
        app = UserActivityDashboard(self)
        app.mainloop()
        self.deiconify()
    # Método para ver perfil de usuario
    def view_profile(self):
        print("Abriendo perfil de usuario...")
        from user_Info import UserProfile, UserProfileWindow

        user = UserProfile(
            username="admin",
            email="admin@correo.com",
            full_name="Administrador General",
            age=30
        )
        self.destroy()
        app = UserProfileWindow(user)
        app.mainloop()
        


if __name__ == "__main__":
>>>>>>> db887b8 (Actualizando interfaces de usuario colores y funciones)
    ct.set_appearance_mode("dark")
    ct.set_default_color_theme("dark-blue")
    dashboard = Dashboard()
    dashboard.mainloop()
