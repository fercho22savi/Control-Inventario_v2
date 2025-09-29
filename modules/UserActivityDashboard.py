import tkinter as tk
import customtkinter as ctk
from datetime import datetime
import os
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
<<<<<<< HEAD

class UserActivityDashboard(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Estética principal (idéntica a login)
        self.title("Panel de Actividad del Usuario")
        self.geometry("800x600")
        self.configure(bg="black")
        self.wm_attributes("-alpha", 0.85)  # Misma transparencia

        # Título
        self.label = ctk.CTkLabel(self, text="Dashboard de Actividad de Usuario", font=("Arial", 20, "bold"))
        self.label.pack(pady=20)

        # Área de texto
        self.text_area = ctk.CTkTextbox(self, width=750, height=200)
        self.text_area.pack(pady=10)

        # Botón actualizar
        self.refresh_button = ctk.CTkButton(self, text="Actualizar Datos", command=self.actualizar_dashboard)
        self.refresh_button.pack(pady=10)

        # Frame para gráfico
        self.graph_frame = ctk.CTkFrame(self, width=750, height=250, fg_color="black")  # Fondo negro uniforme
        self.graph_frame.pack(pady=10)

        self.actualizar_dashboard()

        
    def actualizar_dashboard(self):
        self.cargar_actividades()
        self.mostrar_grafico()

    def cargar_actividades(self):
        self.text_area.delete("1.0", tk.END)
        if not os.path.exists("actividad.log"):
            self.text_area.insert(tk.END, "No hay actividad registrada aún.")
            return

        with open("actividad.log", "r", encoding="utf-8") as file:
            lineas = file.readlines()
            if not lineas:
                self.text_area.insert(tk.END, "El archivo de actividad está vacío.")
            else:
                for linea in lineas[-30:]:
                    self.text_area.insert(tk.END, linea)

    def mostrar_grafico(self):
=======
import platform
import socket
from log_manager import registrar_actividad, leer_actividades, limpiar_log, filtrar_actividades_por_tipo, filtrar_actividades_por_usuario

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

# Clase para el panel de actividad del usuario
class UserActivityDashboard(ctk.CTk):
    def __init__(self, parent=None, usuario="usuario_actual", tipo_usuario="usuario"):
        super().__init__()
        self.parent = parent
        self.usuario = usuario
        self.tipo_usuario = tipo_usuario
        self.session_start = datetime.now()
        
        # Configuración de la ventana principal del Dashboard de Actividad de Usuario
        self.title("Panel de Actividad del Usuario")
        self.geometry("800x600")
        self.configure(fg_color=PALETA["fondo"])
        self.wm_attributes("-alpha", 0.85)

        self.protocol("WM_DELETE_WINDOW", self.back_to_dashboard)
        # Reloj en la esquina superior derecha
        self.clock_label = ctk.CTkLabel(self, font=("Arial", 14))
        self.clock_label.place(relx=1.0, rely=0.0, anchor="ne", x=-10, y=10)
        self.actualizar_reloj()

        self.label = ctk.CTkLabel(self, text="Dashboard de Actividad de Usuario", font=("Arial", 20, "bold"))
        self.label.pack(pady=20)

        self.text_area = ctk.CTkTextbox(self, width=750, height=200)
        self.text_area.pack(pady=10)

        self.button_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.button_frame.pack(pady=5)
        
        button_style = {
            "font": ("Helvetica", 14, "bold"),
            "width": 120,
            "fg_color": PALETA["boton"],
            "text_color": PALETA["texto"],
            "corner_radius": 12,
            "height": 30
        }
        
        # Botón para actualizar datos
        self.refresh_button = ctk.CTkButton(
            self.button_frame, 
            text="Actualizar Datos", 
            command=self.actualizar_dashboard,
            **button_style
        )
        self.refresh_button.grid(row=0, column=0, padx=5)
        # Botón para regresar al dashboard principal
        self.back_button = ctk.CTkButton(
            self.button_frame,
            text="Regresar", 
            command=self.back_to_dashboard,
            **button_style
        )
        self.back_button.grid(row=0, column=1, padx=5)
        # Botón para limpiar el log de actividades
        self.limpiar_button = ctk.CTkButton(
            self.button_frame, text="Limpiar Log", command=self.limpiar_log_button_click,
            **button_style
        )
        self.limpiar_button.grid(row=0, column=2, padx=5)
        # Botón para mostrar logs de admin
        self.admin_logs_button = ctk.CTkButton(
            self.button_frame, 
            text="Mostrar Logs de Admin", 
            command=self.filtrar_logs_admin,
            **button_style
        )
        # Botón para mostrar logs de admin
        self.admin_logs_button.grid(row=0, column=3, padx=5)
        # Botón para mostrar logs de usuario
        self.usuario_logs_button = ctk.CTkButton(
            self.button_frame, 
            text="Mostrar Logs de Usuario",
            command=self.filtrar_logs_usuario,
            **button_style
        )
        self.usuario_logs_button.grid(row=0, column=4, padx=5)
        # Botón para exportar logs a PDF
        self.exportar_button = ctk.CTkButton(
            self.button_frame, 
            text="Exportar Logs a PDF", 
            command=self.exportar_logs_a_pdf,
            **button_style
        )
        self.exportar_button.grid(row=0, column=5, padx=5)
        self.graph_frame = ctk.CTkFrame(self, width=750, height=250, fg_color="black")
        self.graph_frame.pack(pady=10)

        # Registrar la actividad de inicio de sesión
        registrar_actividad(self.usuario, self.tipo_usuario, "Inicio de sesión en el dashboard")
        self.actualizar_dashboard()
    # Método para actualizar el reloj
    def actualizar_reloj(self):
        hora_actual = datetime.now().strftime("%H:%M:%S")
        self.clock_label.configure(text=hora_actual)
        self.after(1000, self.actualizar_reloj)
    # Método para actualizar el dashboard
    def actualizar_dashboard(self):
        self.cargar_actividades()
        self.mostrar_grafico_semana()
    # Método para regresar al dashboard
    def back_to_dashboard(self):
        if self.parent:
            self.parent.deiconify()
        self.destroy()

    # Método para cargar actividades desde el log
    def cargar_actividades(self):
        self.text_area.delete("1.0", tk.END)
        lineas = leer_actividades(ultimas_n=30)
        if not lineas:
            self.text_area.insert(tk.END, "No hay actividad registrada aún.")
        else:
            for linea in lineas:
                self.text_area.insert(tk.END, linea)
    # Método para mostrar gráfico de barras de la semana
    def mostrar_grafico_semana(self):
>>>>>>> db887b8 (Actualizando interfaces de usuario colores y funciones)
        for widget in self.graph_frame.winfo_children():
            widget.destroy()

        if not os.path.exists("actividad.log"):
            return

<<<<<<< HEAD
        acciones = []
        with open("actividad.log", "r", encoding="utf-8") as file:
            for linea in file:
                if ": " in linea:
                    partes = linea.strip().split(": ")
                    if len(partes) == 2:
                        accion = partes[1]
                        acciones.append(accion)

        conteo = Counter(acciones)
        if not conteo:
            return

        # Gráfico con fondo oscuro 
        fig, ax = plt.subplots(figsize=(7, 3))
        fig.patch.set_facecolor("black")
        ax.set_facecolor("black")

        ax.bar(conteo.keys(), conteo.values(), color='deepskyblue')
        ax.set_title("Frecuencia de Actividades", color="white")
        ax.set_ylabel("Cantidad", color="white")
        ax.tick_params(axis='x', labelrotation=45, colors="white")
        ax.tick_params(axis='y', colors="white")
        for spine in ax.spines.values():
            spine.set_color("white")

        fig.tight_layout()

        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()

# Función global para registrar actividad
def registrar_actividad(usuario, accion):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("actividad.log", "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {usuario}: {accion}\n")

# Solo para pruebas individuales
if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    app = UserActivityDashboard()
    app.mainloop()
    app.destroy()
=======
        dias_semana = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        conteo_dias = Counter()

        with open("actividad.log", "r", encoding="utf-8") as file:
            for linea in file:
                if linea.startswith("["):
                    fecha_str = linea.split("]")[0][1:]
                    try:
                        fecha = datetime.strptime(fecha_str, "%Y-%m-%d %H:%M:%S")
                        dia = fecha.strftime("%A")
                        conteo_dias[dia] += 1
                    except ValueError:
                        continue

        valores = [conteo_dias.get(dia, 0) for dia in dias_semana]

        fig, ax = plt.subplots(figsize=(7, 3), facecolor="black")
        ax.set_facecolor("black")
        # Crear gráfico de barras
        bars = ax.bar(dias_semana, valores, color='limegreen')
        ax.set_title("Frecuencia de Actividades por Día de la Semana", color='white', fontsize=14, fontweight='bold')
        ax.set_ylabel("Cantidad", color='white')
        ax.tick_params(axis='x', rotation=45, colors='white')
        ax.tick_params(axis='y', colors='white')
        ax.grid(axis='y', linestyle='--', alpha=0.3)
        # Añadir etiquetas encima de las barras
        for bar, value in zip(bars, valores):
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.1, str(value),
                    ha='center', va='bottom', color='white', fontsize=9)
        # Quitar bordes
        for spine in ax.spines.values():
            spine.set_visible(False)

        fig.tight_layout()
        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()
        
    # Método para limpiar el log de actividades
    def limpiar_log_button_click(self):
        limpiar_log()
        self.text_area.delete("1.0", tk.END)
        self.text_area.insert(tk.END, "El log ha sido limpiado.")

    # Método para filtrar logs de admin
    def filtrar_logs_admin(self):
        logs_admin = filtrar_actividades_por_tipo("admin")
        self.text_area.delete("1.0", tk.END)
        if not logs_admin:
            self.text_area.insert(tk.END, "No hay logs de admin registrados.")
        else:
            for log in logs_admin:
                self.text_area.insert(tk.END, log)
    
    # Método para filtrar logs de usuario
    def filtrar_logs_usuario(self):
        logs_usuario = filtrar_actividades_por_tipo("usuario")
        self.text_area.delete("1.0", tk.END)
        if not logs_usuario:
            self.text_area.insert(tk.END, "No hay logs de usuario registrados.")
        else:
            for log in logs_usuario:
                self.text_area.insert(tk.END, log)

    # Método para exportar logs a PDF
    def exportar_logs_a_pdf(self):
        # Verificar si hay logs para exportar
        if not os.path.exists("actividad.log"):
            self.text_area.delete("1.0", tk.END)
            self.text_area.insert(tk.END, "No hay actividades para exportar.")
            return

        logs = leer_actividades()
        if not logs:
            self.text_area.delete("1.0", tk.END)
            self.text_area.insert(tk.END, "No hay actividades para exportar.")
            return

        try:
            from reportlab.lib.pagesizes import letter
            from reportlab.pdfgen import canvas

            pdf_file = "logs_actividad.pdf"
            c = canvas.Canvas(pdf_file, pagesize=letter)
            width, height = letter

            y_position = height - 40
            for log in logs:
                c.drawString(30, y_position, log.strip())
                y_position -= 15
                if y_position < 40:
                    c.showPage()
                    y_position = height - 40

            c.save()

            self.text_area.delete("1.0", tk.END)
            self.text_area.insert(tk.END, f" Logs exportados a {pdf_file}")
        except Exception as e:
            self.text_area.delete("1.0", tk.END)
            self.text_area.insert(tk.END, f" Error al exportar PDF: {str(e)}")

    # Método para registrar el tiempo en línea del usuario
    def registrar_tiempo_en_linea(self):
        session_end = datetime.now()
        session_duration = session_end - self.session_start
        registrar_actividad(self.usuario, self.tipo_usuario, f"Tiempo en línea: {session_duration}")
    
    # Registrar tiempo en línea al cerrar la ventana
    def destroy(self):
        self.registrar_tiempo_en_linea()
        super().destroy()
        
   

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")
    app = UserActivityDashboard(usuario="Fernando", tipo_usuario="admin")
    app.mainloop()
>>>>>>> db887b8 (Actualizando interfaces de usuario colores y funciones)
