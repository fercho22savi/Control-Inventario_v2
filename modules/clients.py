# -*- coding: utf-8 -*-
# Este módulo es parte de un sistema de gestión de clientes y proveedores.
# Su propósito es permitir la gestión de datos de clientes, incluyendo la adición, actualización y eliminación de registros.
import customtkinter as ct
from tkinter import messagebox
from tkinter import ttk

<<<<<<< HEAD
=======
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from tkinter import filedialog
from reportlab.lib.units import inch
import os
import platform

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
>>>>>>> db887b8 (Actualizando interfaces de usuario colores y funciones)

ct.set_appearance_mode("dark")# Configuración del modo de apariencia
ct.set_default_color_theme("dark-blue")# Configuración del tema de color por defecto

class ClientsApp(ct.CTkToplevel):# Clase para el módulo de clientes
    def __init__(self,master):
        self.master = master
        super().__init__()
        self.title("Módulo de Clientes")
<<<<<<< HEAD
        self.geometry("900x600")
        self.clients = {}
        self.current_id = None

        title_label = ct.CTkLabel(self, text="Clientes", font=ct.CTkFont(size=28, weight="bold"))
        title_label.pack(padx=20, pady=(20, 5), anchor="w")

        # Frame de formulario clientes
        form_frame = ct.CTkFrame(self, fg_color="transparent")
        form_frame.pack(pady=10, padx=10, fill="x")

        form_frame.grid_columnconfigure((0, 1, 2), weight=0)# Configuración de columnas del frame

        self.id_entry = self._add_entry(form_frame, "ID:", 0, 0)
        self.name_entry = self._add_entry(form_frame, "Nombre:", 0, 2)
        self.phone_entry = self._add_entry(form_frame, "Teléfono:", 1, 0)
        self.email_entry = self._add_entry(form_frame, "Email:", 1, 2)
        self.product_entry = self._add_entry(form_frame, "Producto:", 2, 0)
        self.quantity_entry = self._add_entry(form_frame, "Cantidad:", 2, 2)

    
=======
        self.geometry("1000x600")
        self.configure(fg_color=PALETA["panel"])
        self.wm_attributes("-alpha", 0.85)
        self.clients = {}
        self.current_id = None
        

        title_label = ct.CTkLabel(self, text="Clientes", font=ct.CTkFont(size=28, weight="bold"))# Etiqueta de título
        title_label.pack(padx=15, pady=(20, 5), anchor="w")# Configuración de la etiqueta de título

        # Frame de formulario clientes
        form_frame = ct.CTkFrame(self, fg_color="transparent")
        form_frame.pack(pady=10, padx=10, fill="x", expand=True)  # Configuración del frame de formulario

        form_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)  # Configuración de columnas del frame

        self.id_entry = self._add_entry(form_frame, "ID:", 0, 0)  
        self.name_entry = self._add_entry(form_frame, "Nombre:", 0, 2)
        self.surname_entry = self._add_entry(form_frame, "Apellido:", 1, 0)
        self.phone_entry = self._add_entry(form_frame, "Teléfono:", 1, 2)
        self.address_entry = self._add_entry(form_frame, "Dirección:", 2, 0)  
        self.email_entry = self._add_entry(form_frame, "Email:", 2, 2)
        self.product_entry = self._add_entry(form_frame, "Producto:", 3, 0)
        self.quantity_entry = self._add_entry(form_frame, "Cantidad:", 3, 2)
      
>>>>>>> db887b8 (Actualizando interfaces de usuario colores y funciones)

        # Botones
        button_frame = ct.CTkFrame(self, fg_color="transparent")
        button_frame.pack(pady=10)
<<<<<<< HEAD
        ct.CTkButton(button_frame, text="Agregar", width=140, command=self.add_client).grid(row=0, column=0, padx=5)
        ct.CTkButton(button_frame, text="Actualizar", width=140, command=self.update_client).grid(row=0, column=1, padx=5)
        ct.CTkButton(button_frame, text="Eliminar", width=140, command=self.delete_client).grid(row=0, column=2, padx=5)
        ct.CTkButton(button_frame, text="Limpiar", width=140, command=self.clear_entries).grid(row=0, column=3, padx=5)
        ct.CTkButton(button_frame, text="Regresar", width=140, command=self.back_to_dashboard).grid(row=0, column=4, padx=5)

        # Tabla
        self.clients_table = ttk.Treeview(
            self, columns=("ID", "Nombre", "Teléfono", "Email", "Producto", "Cantidad"),
            show="headings", height=10
        )
        for col in self.clients_table["columns"]:# Configuración de columnas de la tabla
            self.clients_table.heading(col, text=col)
            self.clients_table.column(col, anchor="center", width=120)

        self.clients_table.pack(pady=10, padx=10, fill="both", expand=True)# Tabla ocupa todo el espacio disponible
        self.clients_table.bind("<Double-1>", self.on_item_selected)# Evento de doble clic para seleccionar un cliente

        self._style_table()# Método para aplicar estilo a la tabla

    def _add_entry(self, parent, label, row, column):# Método para crear entradas con etiquetas
        ct.CTkLabel(parent, text=label).grid(row=row, column=column, padx=10, pady=5, sticky="e")
        entry = ct.CTkEntry(parent, width=180)
        entry.grid(row=row, column=column + 1, padx=10, pady=5)
=======
        
             # Configuración base para los botones
        button_style = {
            "font": ("Helvetica", 14, "bold"),
            "width": 120,
            "fg_color": PALETA["boton"],
            "text_color": PALETA["texto"],
            "corner_radius": 12,
            "height": 30
        }

        ct.CTkButton(button_frame, text="Agregar", command=self.add_client, **button_style).grid(row=0, column=0, padx=5)
        ct.CTkButton(button_frame, text="Actualizar", command=self.update_clients, **button_style).grid(row=0, column=1, padx=5)
        ct.CTkButton(button_frame, text="Eliminar", command=self.delete_client, **button_style).grid(row=0, column=2, padx=5)
        ct.CTkButton(button_frame, text="Limpiar", command=self.clear_entries, **button_style).grid(row=0, column=3, padx=5)
        ct.CTkButton(button_frame, text="Generar PDF", command=self.export_to_pdf, **button_style).grid(row=0, column=4, padx=5)
        ct.CTkButton(button_frame, text="Regresar", command=self.back_to_dashboard, **button_style).grid(row=0, column=5, padx=5)

        # Tabla de clientes
        self.clients_table = ttk.Treeview(
            self, columns=("ID", "Nombre", "Apellido", "Teléfono","Dirección", "Email", "Producto", "Cantidad"),
            show="headings", height=10
        )
        column_widths = {
            "ID": 80,
            "Nombre": 110,
            "Apellido": 120,
            "Teléfono": 100,
            "Dirección": 200,
            "Email": 140,
            "Producto": 140,
            "Cantidad": 100
            
        }
        for col in self.clients_table["columns"]:  # Configuración de columnas de la tabla
            self.clients_table.heading(col, text=col)
            self.clients_table.column(col, anchor="center", width=column_widths[col], stretch=False)

        self.clients_table.pack(pady=10, padx=10, fill="both", expand=True)  # Tabla ocupa todo el espacio disponible
        self.clients_table.bind("<Double-1>", self.on_item_selected)  # Evento de doble clic para seleccionar un cliente

        self._style_table()  # Método para aplicar estilo a la tabla

    def _add_entry(self, parent, label, row, column):# Método para crear entradas con etiquetas
        ct.CTkLabel(parent, text=label).grid(row=row, column=column, padx=10, pady=5, sticky="e")
        entry = ct.CTkEntry(parent, width=200, height=30, corner_radius=8)
        entry.grid(row=row, column=column + 1, padx=8, pady=5)
>>>>>>> db887b8 (Actualizando interfaces de usuario colores y funciones)
        return entry

    def _style_table(self):# Método para aplicar estilo a la tabla
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", background="#1a1a1a", foreground="white", fieldbackground="#1a1a1a", rowheight=30, font=('Arial', 11))
        style.configure("Treeview.Heading", background="#2A9D8F", foreground="white", font=('Arial', 11, 'bold'))
        style.map("Treeview", background=[('selected', '#21867A')], foreground=[('selected', 'white')])

    def _add_entry(self, parent, label_text, row, column):# Método para crear entradas con etiquetas
         label = ct.CTkLabel(parent, text=label_text, font=ct.CTkFont(size=14))
         label.grid(row=row, column=column, sticky="e", padx=(5, 2), pady=8)

         entry = ct.CTkEntry(parent, width=200, height=30, corner_radius=8)
         entry.grid(row=row, column=column + 1, padx=(2, 10), pady=8)
         return entry


    def populate_table(self):# Método para llenar la tabla con datos de clientes
        for row in self.clients_table.get_children():
            self.clients_table.delete(row)
        for client_id, data in self.clients.items():
            self.clients_table.insert("", "end", values=(
<<<<<<< HEAD
                client_id, data["nombre"], data["telefono"],
=======
                client_id, data["nombre"], data["apellido"], data["telefono"], data["direccion"],
>>>>>>> db887b8 (Actualizando interfaces de usuario colores y funciones)
                data["correo"], data["producto"], data["cantidad"]
            ))

    def add_client(self):# Método para agregar un nuevo cliente
        client_id = self.id_entry.get()
        if client_id in self.clients:
            messagebox.showerror("Error", "El ID ya existe.")
            return
        self.clients[client_id] = {
<<<<<<< HEAD
            "nombre": self.name_entry.get(),
            "telefono": self.phone_entry.get(),
            "correo": self.email_entry.get(),
            "producto": self.product_entry.get(),
            "cantidad": self.quantity_entry.get()
=======
            "id": self.id_entry.get(),
            "nombre": self.name_entry.get(),
            "apellido": self.surname_entry.get(),
            "telefono": self.phone_entry.get(),
            "direccion": self.address_entry.get(),
            "correo": self.email_entry.get(),
            "producto": self.product_entry.get(),
            "cantidad": self.quantity_entry.get()
            
>>>>>>> db887b8 (Actualizando interfaces de usuario colores y funciones)
        }
        self.populate_table()
        self.clear_entries()

<<<<<<< HEAD
    def update_client(self):# Método para actualizar un cliente existente
        if self.current_id is None:
            messagebox.showerror("Error", "Seleccione un cliente para actualizar.")
            return

        self.clients[self.current_id] = {
            "nombre": self.name_entry.get(),
            "telefono": self.phone_entry.get(),
            "correo": self.email_entry.get(),
            "producto": self.product_entry.get(),
            "cantidad": self.quantity_entry.get()
        }
        self.populate_table()# Actualiza la tabla con los nuevos datos
        self.clear_entries()

    def delete_client(self):# Método para eliminar un cliente
        if self.current_id is None:
            messagebox.showerror("Error", "Seleccione un cliente para eliminar.")
            return
        if messagebox.askyesno("Confirmar", "¿Está seguro de que desea eliminar este cliente?"):
            del self.clients[self.current_id]
            self.populate_table()
            self.clear_entries()
            messagebox.showinfo("Éxito", "¡Cliente eliminado exitosamente!")
        messagebox.showinfo("Éxito", "¡Cliente eliminado exitosamente!")
        if messagebox.askyesno("Confirmar", "¿Está seguro de que desea eliminar este cliente?"):
            del self.clients[self.current_id]
            self.populate_table()
            self.clear_entries()
            messagebox.showinfo("Éxito", "¡Cliente eliminado exitosamente!")
=======
    def update_clients(self):
    # Cargar datos del cliente seleccionado a los campos de entrada
      selected = self.clients_table.selection()  # Cambiar 'self.tree' a 'self.clients_table'
      if selected:
        values = self.clients_table.item(selected)['values']
        if values:
            self.id_entry.configure(state="disabled")  # Cargar el ID del cliente seleccionado disabled para evitar cambios
            self.id_entry.delete(0, 'end')
            self.id_entry.insert(0, values[0])
            self.name_entry.delete(0, 'end')
            self.name_entry.insert(0, values[1])
            self.surname_entry.delete(0, 'end')
            self.surname_entry.insert(0, values[2])
            self.phone_entry.delete(0, 'end')
            self.phone_entry.insert(0, values[3])
            self.address_entry.delete(0, 'end')
            self.address_entry.insert(0, values[4])
            self.email_entry.delete(0, 'end')
            self.email_entry.insert(0, values[5])
            self.product_entry.delete(0, 'end')
            self.product_entry.insert(0, values[6])
            self.quantity_entry.delete(0, 'end')
            self.quantity_entry.insert(0, values[7])
            
            self.current_id = selected  # Guardar cuál es el cliente seleccionado
      else:
        messagebox.showwarning("Selecciona", "Selecciona un cliente de la tabla.")

    # Método para eliminar un cliente seleccionado
    def delete_client(self):# Método para eliminar un cliente
        selected_item = self.clients_table.selection()
        if not selected_item:
            messagebox.showwarning("Seleccionar", "Selecciona un cliente para eliminar.")
            return
        client_id = self.clients_table.item(selected_item)["values"][0]
        if client_id in self.clients:
            del self.clients[client_id]
        else:
            messagebox.showerror("Error", "El cliente no existe.")
        self.populate_table()
        self.clear_entries()
>>>>>>> db887b8 (Actualizando interfaces de usuario colores y funciones)

    def on_item_selected(self, event):# Método para manejar la selección de un cliente en la tabla
        selected_item = self.clients_table.selection()[0]
        values = self.clients_table.item(selected_item, "values")
        self.current_id = values[0]
        self.id_entry.delete(0, ct.END)
        self.id_entry.insert(0, values[0])
        self.name_entry.delete(0, ct.END)
        self.name_entry.insert(0, values[1])
<<<<<<< HEAD
        self.phone_entry.delete(0, ct.END)
        self.phone_entry.insert(0, values[2])
        self.email_entry.delete(0, ct.END)
        self.email_entry.insert(0, values[3])
        self.product_entry.delete(0, ct.END)
        self.product_entry.insert(0, values[4])
        self.quantity_entry.delete(0, ct.END)
        self.quantity_entry.insert(0, values[5])

    def clear_entries(self):# Método para limpiar los campos de entrada
        for entry in [self.id_entry, self.name_entry, self.phone_entry,
                      self.email_entry, self.product_entry, self.quantity_entry]:
=======
        self.surname_entry.delete(0, ct.END)
        self.surname_entry.insert(0, values[2])
        self.phone_entry.delete(0, ct.END)
        self.phone_entry.insert(0, values[3])
        self.email_entry.delete(0, ct.END)
        self.email_entry.insert(0, values[4])
        self.product_entry.delete(0, ct.END)
        self.product_entry.insert(0, values[5])
        self.quantity_entry.delete(0, ct.END)
        self.quantity_entry.insert(0, values[6])
        self.address_entry.delete(0, ct.END)
        self.address_entry.insert(0, values[7])

    def clear_entries(self):# Método para limpiar los campos de entrada
        for entry in [self.id_entry, self.name_entry, self.surname_entry, self.phone_entry,
                      self.email_entry, self.product_entry, self.quantity_entry, self.address_entry]:
>>>>>>> db887b8 (Actualizando interfaces de usuario colores y funciones)
            entry.delete(0, ct.END)
        self.current_id = None

    def back_to_dashboard(self):
        self.destroy()
        self.master.deiconify()

<<<<<<< HEAD
=======
    def export_to_pdf(self):  # Método para exportar la tabla a PDF con formato ajustable
        if not self.clients_table.get_children():  # Verificar si la tabla tiene datos
            messagebox.showwarning("Advertencia", "No hay datos en la tabla para exportar.")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".pdf",
                                                 filetypes=[("PDF files", "*.pdf")],
                                                 title="Guardar como")
        if not file_path:
            return

        columns = self.clients_table["columns"]
        num_columns = len(columns)

        # Determinar orientación de la página
        if num_columns > 6:  # Si hay más de 6 columnas, usar orientación horizontal
            page_size = letter[1], letter[0]  # Ancho y alto invertidos
        else:
            page_size = letter

        c = canvas.Canvas(file_path, pagesize=page_size)
        width, height = page_size

        # Título principal
        c.setFont("Helvetica-Bold", 18)
        c.drawString(50, height - 50, "Listado de Clientes")

        # Logo (si tienes uno llamado "logo.png" en el mismo directorio)
        try:
            c.drawImage("logo.png", width - 120, height - 80, width=60, height=60, preserveAspectRatio=True, mask='auto')
        except Exception as e:
            print("No se pudo cargar el logo:", e)

        # Encabezados de tabla
        c.setFont("Helvetica-Bold", 10)
        x = 50
        y = height - 100
        column_width = (width - 100) / num_columns  # Ajustar ancho de columna dinámicamente
        for i, col in enumerate(columns):
            c.drawString(x + i * column_width, y, str(col))

        y -= 15
        c.setFont("Helvetica", 9)

        # Filas
        for row in self.clients_table.get_children():# Obtener cada fila de la tabla
            values = self.clients_table.item(row, "values")
            for i, value in enumerate(values):
                c.drawString(x + i * column_width, y, str(value))
            y -= 15
            if y < 50:
                c.showPage()
                y = height - 50
                c.setFont("Helvetica-Bold", 10)
                for i, col in enumerate(columns):
                    c.drawString(x + i * column_width, y, str(col))
                y -= 15
                c.setFont("Helvetica", 9)

        c.save()

        # Abrir automáticamente el archivo
        try:
            if platform.system() == 'Darwin':  # macOS
                os.system(f"open '{file_path}'")
            elif platform.system() == 'Windows':  # Windows
                os.startfile(file_path)
            else:  # Linux
                os.system(f"xdg-open '{file_path}'")
        except Exception as e:
            print("No se pudo abrir el archivo automáticamente:", e)

>>>>>>> db887b8 (Actualizando interfaces de usuario colores y funciones)

if __name__ == "__main__":
    root = ct.CTk()
    app = ClientsApp(root)
    root.mainloop()
