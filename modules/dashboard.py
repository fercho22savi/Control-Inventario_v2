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
        ct.CTkButton(
            self,
            text="Módulo Proveedores",
            command=self.open_suppliers_module,
            **button_style
        ).pack(pady=15)

        ct.CTkButton(
            self,
            text="Módulo Clientes",
            command=self.open_clients_module,
            **button_style
        ).pack(pady=15)

        ct.CTkButton(
            self,
            text="Módulo Productos",
            command=self.open_products_module,
            **button_style
        ).pack(pady=15)

        ct.CTkButton(
            self,
            text="Administrar Usuarios",
            command=self.open_user_activity_module,
            **button_style
        ).pack(pady=15)

        ct.CTkButton(
            self,
            text="Ver Perfil",
            command=self.view_profile,
            **button_style
        ).pack(pady=15)

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
        print("Abriendo módulo de proveedores...")
        self.withdraw()
        app = SuppliersApp(self)
        app.mainloop()
        self.deiconify()

    # Método para abrir el módulo de clientes
    def open_clients_module(self):
        print("Abriendo módulo de clientes...")
        self.withdraw()
        app = ClientsApp(self)
        app.mainloop()
        self.deiconify()

    # Método para abrir el módulo de productos
    def open_products_module(self):
        print("Abriendo módulo de productos...")
        self.withdraw()
        app = ProductApp(self)
        app.mainloop()
        self.deiconify()

    # Método para regresar al dashboard
    def back_to_dashboard(self):
        print("Regresando al Dashboard...")
        self.destroy()
        dashboard = Dashboard()
        dashboard.mainloop()

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
    ct.set_appearance_mode("dark")
    ct.set_default_color_theme("dark-blue")
    dashboard = Dashboard()
    dashboard.mainloop()
