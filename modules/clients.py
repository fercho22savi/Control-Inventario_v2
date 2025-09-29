# -*- coding: utf-8 -*-
# Este módulo es parte de un sistema de gestión de clientes y proveedores.
# Su propósito es permitir la gestión de datos de clientes, incluyendo la adición, actualización y eliminación de registros.

import customtkinter as ct
from tkinter import messagebox
from tkinter import ttk
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from tkinter import filedialog
import os
import platform

# Paleta de colores
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

ct.set_appearance_mode("dark")  # Configuración del modo de apariencia
ct.set_default_color_theme("dark-blue")  # Configuración del tema de color por defecto


class ClientsApp(ct.CTkToplevel):  # Clase para el módulo de clientes
    def __init__(self, master):
        self.master = master
        super().__init__()
        self.title("Módulo de Clientes")
        self.geometry("1000x600")
        self.configure(fg_color=PALETA["panel"])
        self.wm_attributes("-alpha", 0.85)

        self.clients = {}
        self.current_id = None

        # Título
        title_label = ct.CTkLabel(self, text="Clientes", font=ct.CTkFont(size=28, weight="bold"))
        title_label.pack(padx=15, pady=(20, 5), anchor="w")

        # Frame de formulario clientes
        form_frame = ct.CTkFrame(self, fg_color="transparent")
        form_frame.pack(pady=10, padx=10, fill="x", expand=True)
        form_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)

        # Entradas del formulario
        self.id_entry = self._add_entry(form_frame, "ID:", 0, 0)
        self.name_entry = self._add_entry(form_frame, "Nombre:", 0, 2)
        self.surname_entry = self._add_entry(form_frame, "Apellido:", 1, 0)
        self.phone_entry = self._add_entry(form_frame, "Teléfono:", 1, 2)
        self.address_entry = self._add_entry(form_frame, "Dirección:", 2, 0)
        self.email_entry = self._add_entry(form_frame, "Email:", 2, 2)
        self.product_entry = self._add_entry(form_frame, "Producto:", 3, 0)
        self.quantity_entry = self._add_entry(form_frame, "Cantidad:", 3, 2)

        # Botones
        button_style = {
            "font": ("Helvetica", 14, "bold"),
            "width": 120,
            "fg_color": PALETA["boton"],
            "text_color": PALETA["texto"],
            "corner_radius": 12,
            "height": 30
        }

        button_frame = ct.CTkFrame(self, fg_color="transparent")
        button_frame.pack(pady=10)

        ct.CTkButton(button_frame, text="Agregar", command=self.add_client, **button_style).grid(row=0, column=0, padx=5)
        ct.CTkButton(button_frame, text="Actualizar", command=self.update_clients, **button_style).grid(row=0, column=1, padx=5)
        ct.CTkButton(button_frame, text="Eliminar", command=self.delete_client, **button_style).grid(row=0, column=2, padx=5)
        ct.CTkButton(button_frame, text="Limpiar", command=self.clear_entries, **button_style).grid(row=0, column=3, padx=5)
        ct.CTkButton(button_frame, text="Generar PDF", command=self.export_to_pdf, **button_style).grid(row=0, column=4, padx=5)
        ct.CTkButton(button_frame, text="Regresar", command=self.back_to_dashboard, **button_style).grid(row=0, column=5, padx=5)

        # Tabla de clientes
        self.clients_table = ttk.Treeview(
            self, columns=("ID", "Nombre", "Apellido", "Teléfono", "Dirección", "Email", "Producto", "Cantidad"),
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

        for col in self.clients_table["columns"]:
            self.clients_table.heading(col, text=col)
            self.clients_table.column(col, anchor="center", width=column_widths[col], stretch=False)

        self.clients_table.pack(pady=10, padx=10, fill="both", expand=True)
        self.clients_table.bind("<Double-1>", self.on_item_selected)

        self._style_table()

    # Método auxiliar para crear campos de entrada con etiqueta
    def _add_entry(self, parent, label, row, column):
        ct.CTkLabel(parent, text=label).grid(row=row, column=column, padx=10, pady=5, sticky="e")
        entry = ct.CTkEntry(parent, width=200, height=30, corner_radius=8)
        entry.grid(row=row, column=column + 1, padx=8, pady=5)
        return entry

    # Estilos de la tabla
    def _style_table(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure(
            "Treeview",
            background="#1a1a1a",
            foreground="white",
            fieldbackground="#1a1a1a",
            rowheight=30,
            font=('Arial', 11)
        )
        style.configure("Treeview.Heading", background="#2A9D8F", foreground="white", font=('Arial', 11, 'bold'))
        style.map("Treeview", background=[('selected', '#21867A')], foreground=[('selected', 'white')])

    # Poblar tabla
    def populate_table(self):
        for row in self.clients_table.get_children():
            self.clients_table.delete(row)
        for client_id, data in self.clients.items():
            self.clients_table.insert("", "end", values=(
                client_id, data.get("nombre", ""), data.get("apellido", ""), data.get("telefono", ""),
                data.get("direccion", ""), data.get("correo", ""), data.get("producto", ""), data.get("cantidad", "")
            ))

    # Agregar cliente
    def add_client(self):
        client_id = self.id_entry.get()
        if client_id in self.clients:
            messagebox.showerror("Error", "El ID ya existe.")
            return
        self.clients[client_id] = {
            "id": self.id_entry.get(),
            "nombre": self.name_entry.get(),
            "apellido": self.surname_entry.get(),
            "telefono": self.phone_entry.get(),
            "direccion": self.address_entry.get(),
            "correo": self.email_entry.get(),
            "producto": self.product_entry.get(),
            "cantidad": self.quantity_entry.get()
        }
        self.populate_table()
        self.clear_entries()

    # Cargar datos de un cliente para editar
    def update_clients(self):
        selected = self.clients_table.selection()
        if selected:
            values = self.clients_table.item(selected)['values']
            if values:
                self.id_entry.configure(state="disabled")
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
                self.current_id = values[0]
        else:
            messagebox.showwarning("Selecciona", "Selecciona un cliente de la tabla.")

    # Eliminar cliente
    def delete_client(self):
        selected_item = self.clients_table.selection()
        if not selected_item:
            messagebox.showwarning("Seleccionar", "Selecciona un cliente para eliminar.")
            return
        client_id = self.clients_table.item(selected_item)["values"][0]
        if client_id in self.clients:
            del self.clients[client_id]
            self.populate_table()
            self.clear_entries()
            messagebox.showinfo("Éxito", "¡Cliente eliminado exitosamente!")
        else:
            messagebox.showerror("Error", "El cliente no existe.")

    # Evento al seleccionar un cliente en la tabla
    def on_item_selected(self, event):
        selected_item = self.clients_table.selection()[0]
        values = self.clients_table.item(selected_item, "values")
        self.current_id = values[0]
        self.id_entry.delete(0, ct.END)
        self.id_entry.insert(0, values[0])
        self.name_entry.delete(0, ct.END)
        self.name_entry.insert(0, values[1])
        self.surname_entry.delete(0, ct.END)
        self.surname_entry.insert(0, values[2])
        self.phone_entry.delete(0, ct.END)
        self.phone_entry.insert(0, values[3])
        self.address_entry.delete(0, ct.END)
        self.address_entry.insert(0, values[4])
        self.email_entry.delete(0, ct.END)
        self.email_entry.insert(0, values[5])
        self.product_entry.delete(0, ct.END)
        self.product_entry.insert(0, values[6])
        self.quantity_entry.delete(0, ct.END)
        self.quantity_entry.insert(0, values[7])

    # Limpiar entradas
    def clear_entries(self):
        for entry in [self.id_entry, self.name_entry, self.surname_entry,
                      self.phone_entry, self.address_entry, self.email_entry,
                      self.product_entry, self.quantity_entry]:
            entry.delete(0, ct.END)
        self.id_entry.configure(state="normal")
        self.current_id = None

    # Volver al dashboard
    def back_to_dashboard(self):
        self.destroy()
        self.master.deiconify()

    # Exportar tabla a PDF
    def export_to_pdf(self):
        if not self.clients_table.get_children():
            messagebox.showwarning("Advertencia", "No hay datos en la tabla para exportar.")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".pdf",
                                                 filetypes=[("PDF files", "*.pdf")],
                                                 title="Guardar como")
        if not file_path:
            return

        columns = self.clients_table["columns"]
        num_columns = len(columns)

        # Orientación
        if num_columns > 6:
            page_size = (letter[1], letter[0])
        else:
            page_size = letter

        c = canvas.Canvas(file_path, pagesize=page_size)
        width, height = page_size

        # Título
        c.setFont("Helvetica-Bold", 18)
        c.drawString(50, height - 50, "Listado de Clientes")

        # Encabezados
        c.setFont("Helvetica-Bold", 10)
        x = 50
        y = height - 100
        column_width = (width - 100) / num_columns
        for i, col in enumerate(columns):
            c.drawString(x + i * column_width, y, str(col))

        y -= 15
        c.setFont("Helvetica", 9)

        # Filas
        for row in self.clients_table.get_children():
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

        try:
            if platform.system() == 'Darwin':
                os.system(f"open '{file_path}'")
            elif platform.system() == 'Windows':
                os.startfile(file_path)
            else:
                os.system(f"xdg-open '{file_path}'")
        except Exception as e:
            print("No se pudo abrir el archivo automáticamente:", e)


if __name__ == "__main__":
    root = ct.CTk()
    app = ClientsApp(root)
    root.mainloop()
