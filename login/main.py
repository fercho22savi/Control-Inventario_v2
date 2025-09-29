# main.py
import tkinter as tk
import customtkinter as ctk

from login import LoginModerno   # Importar tu login
from dashboard import Dashboard  # Importar el Dashboard


def main():
    # Configuración de CustomTkinter
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    # Crear la ventana raíz de Tkinter
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana raíz

    # Crear login
    login = LoginModerno(root)

    # Sobrescribir el método para abrir el dashboard al iniciar sesión
    def abrir_dashboard():
        login.destroy()
        dashboard = Dashboard()
        dashboard.mainloop()

    login.to_dashboard = abrir_dashboard

    login.mainloop()


if __name__ == "__main__":
    main()
