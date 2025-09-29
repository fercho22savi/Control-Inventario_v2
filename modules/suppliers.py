import customtkinter as ctk
from tkinter import messagebox
from tkinter import ttk

<<<<<<< HEAD
class SuppliersApp(ctk.CTkToplevel):
    def __init__(self, master):
=======
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
# Modulo de gestión de proveedores
class SuppliersApp(ctk.CTkToplevel):
    def __init__(self, master): 
>>>>>>> db887b8 (Actualizando interfaces de usuario colores y funciones)
        super().__init__(master)
        self.master = master
        self.title("Gestión de Proveedores")
        self.geometry("900x600")
<<<<<<< HEAD
        self.configure(fg_color="#121212")

        self.suppliers = {}
        self.current_id = None
=======
        self.configure(fg_color=PALETA["fondo"])
        self.wm_attributes("-alpha", 0.85)

        self.suppliers = {} # Diccionario para almacenar los proveedores
        self.current_id = None # ID del proveedor actualmente seleccionado
>>>>>>> db887b8 (Actualizando interfaces de usuario colores y funciones)

        # Estilo oscuro para la tabla
        style = ttk.Style()
        style.theme_use("default")
<<<<<<< HEAD
        style.configure("Treeview",
                        background="#1E1E1E",
                        foreground="white",
                        fieldbackground="#1E1E1E",
=======
        style.configure("Treeview", 
                        background=PALETA["panel"],
                        foreground=PALETA["texto"],
                        fieldbackground=PALETA["panel"],
>>>>>>> db887b8 (Actualizando interfaces de usuario colores y funciones)
                        rowheight=28,
                        font=("Arial", 12))
        style.configure("Treeview.Heading",
                        background="#2A9D8F",
                        foreground="white",
                        font=("Arial", 12, "bold"))
        style.map("Treeview",
                  background=[("selected", "#21867A")],
                  foreground=[("selected", "white")])

        self.create_widgets()
        self.populate_table()
<<<<<<< HEAD

    def create_widgets(self):
        form_frame = ctk.CTkFrame(self, fg_color="#1C1C1C")
        form_frame.pack(pady=15, padx=20, fill="x")

        # Entradas
        self.id_entry = self.create_labeled_entry(form_frame, "ID:", 0)
        self.name_entry = self.create_labeled_entry(form_frame, "Nombre:", 1)
        self.surname_entry = self.create_labeled_entry(form_frame, "Apellido:", 2)
        self.phone_entry = self.create_labeled_entry(form_frame, "Teléfono:", 3)
        self.address_entry = self.create_labeled_entry(form_frame, "Dirección:", 4)

        # Botones
        button_frame = ctk.CTkFrame(self, fg_color="#121212")
        button_frame.pack(pady=10)

        ctk.CTkButton(button_frame, text="Agregar", width=140, command=self.add_supplier).grid(row=0, column=0, padx=6)
        ctk.CTkButton(button_frame, text="Actualizar", width=140, command=self.update_supplier).grid(row=0, column=1, padx=6)
        ctk.CTkButton(button_frame, text="Eliminar", width=140, command=self.delete_supplier).grid(row=0, column=2, padx=6)
        ctk.CTkButton(button_frame, text="Limpiar", width=140, command=self.clear_entries).grid(row=0, column=3, padx=6)
        ctk.CTkButton(button_frame, text="Regresar", width=140, command=self.back_to_dashboard).grid(row=0, column=4, padx=6)

        # Tabla
        self.suppliers_table = ttk.Treeview(self, columns=("ID", "Nombre", "Apellido", "Teléfono", "Dirección"), show='headings')
        for col in ("ID", "Nombre", "Apellido", "Teléfono", "Dirección"):
            self.suppliers_table.heading(col, text=col)
            self.suppliers_table.column(col, anchor="center", width=120)

        self.suppliers_table.pack(pady=20, padx=20, fill="both", expand=True)
        self.suppliers_table.bind("<Double-1>", self.on_item_selected)

    def create_labeled_entry(self, parent, text, row):
=======
    # Método para crear los widgets de la interfaz
    def create_widgets(self):
        form_frame = ctk.CTkFrame(self, fg_color=PALETA["panel"])
        form_frame.pack(pady=15, padx=20, fill="x")

        # Entradas de datos
        self.id_entry = self.create_labeled_entry(form_frame, "ID:", 0)
        self.name_entry = self.create_labeled_entry(form_frame, "Nombre proveedor:", 1)
        self.nit_entry = self.create_labeled_entry(form_frame, "Nit:", 2)

        self.phone_entry = self.create_labeled_entry(form_frame, "Teléfono:", 3)
        self.address_entry = self.create_labeled_entry(form_frame, "Dirección:", 4)
        self.city_entry = self.create_labeled_entry(form_frame, "Ciudad:", 5)

        # Botones de acción 
        button_frame = ctk.CTkFrame(self, fg_color="#121212")
        button_frame.pack(pady=10)
        
          # Configuración base para los botones
        button_style = {
            "font": ("Helvetica", 14, "bold"),
            "width": 120,
            "fg_color": PALETA["boton"],
            "text_color": PALETA["texto"],
            "corner_radius": 12,
            "height": 30
        }

        ctk.CTkButton(button_frame, text="Agregar", command=self.add_supplier, **button_style).grid(row=0, column=0, padx=4)
        ctk.CTkButton(button_frame, text="Editar", command=self.update_supplier, **button_style).grid(row=0, column=1, padx=4)
        ctk.CTkButton(button_frame, text="Actualizar", command=self.apply_supplier_update, **button_style).grid(row=0, column=2, padx=4)
        ctk.CTkButton(button_frame, text="Eliminar", command=self.delete_supplier, **button_style).grid(row=0, column=3, padx=4)
        ctk.CTkButton(button_frame, text="Limpiar", command=self.clear_entries, **button_style).grid(row=0, column=4, padx=4)
        ctk.CTkButton(button_frame, text="Regresar", command=self.back_to_dashboard, **button_style).grid(row=0, column=5, padx=4)

        
        # Tabla de proveedores
        self.suppliers_table = ttk.Treeview(self, columns=("ID", "Nombre proveedor", "Nit", "Teléfono", "Dirección", "Ciudad"), show='headings')
        for col in ("ID", "Nombre proveedor", "Nit", "Teléfono", "Dirección", "Ciudad"):
            self.suppliers_table.heading(col, text=col)
            self.suppliers_table.column(col, anchor="center", width=120)

        self.suppliers_table.pack(pady=5, padx=20, fill="both", expand=True)
        self.suppliers_table.bind("<Double-1>", self.on_item_selected)


     # Método para crear entradas con etiquetas  
    def create_labeled_entry(self, parent, text, row):# Método para crear entradas con etiquetas
>>>>>>> db887b8 (Actualizando interfaces de usuario colores y funciones)
        label = ctk.CTkLabel(parent, text=text, text_color="white")
        label.grid(row=row, column=0, sticky="w", padx=10, pady=8)
        entry = ctk.CTkEntry(parent, width=300)
        entry.grid(row=row, column=1, pady=8)
        return entry

<<<<<<< HEAD
=======
    # Método para llenar la tabla con los datos de los proveedores
>>>>>>> db887b8 (Actualizando interfaces de usuario colores y funciones)
    def populate_table(self):
        for row in self.suppliers_table.get_children():
            self.suppliers_table.delete(row)
        for supplier_id, data in self.suppliers.items():
<<<<<<< HEAD
            self.suppliers_table.insert("", "end", values=(supplier_id, data["name"], data["surname"], data["phone"], data["address"]))

    def add_supplier(self):
        supplier_id = self.id_entry.get().strip()
        name = self.name_entry.get().strip()
        surname = self.surname_entry.get().strip()
        phone = self.phone_entry.get().strip()
        address = self.address_entry.get().strip()

        if supplier_id in self.suppliers:
            messagebox.showerror("Error", "El ID ya existe.")
            return

        if not supplier_id or not name or not surname or not phone or not address:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")
            return

        self.suppliers[supplier_id] = {"name": name, "surname": surname, "phone": phone, "address": address}
=======
            self.suppliers_table.insert("", "end", values=(supplier_id, data["name"], 
                                                           data["nit"], data["phone"], data["address"], data["city"]))

    # Método para agregar un nuevo proveedor
    def add_supplier(self):
        supplier_id = self.id_entry.get().strip()
        name = self.name_entry.get().strip()
        nit = self.nit_entry.get().strip()
        phone = self.phone_entry.get().strip()
        address = self.address_entry.get().strip()
        city = self.city_entry.get().strip()

        if supplier_id in self.suppliers:# Verifica si el ID ya existe
            messagebox.showerror("Error", "El ID ya existe.")
            return

        if not supplier_id or not name or not nit or not phone or not address or not city:# Verifica si los campos están vacíos
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")
            return

        self.suppliers[supplier_id] = {"name": name, "nit": nit, "phone": phone, "address": address, "city": city}
>>>>>>> db887b8 (Actualizando interfaces de usuario colores y funciones)
        self.populate_table()
        self.clear_entries()
        messagebox.showinfo("Éxito", "¡Proveedor agregado exitosamente!")

<<<<<<< HEAD
    def update_supplier(self):
        if self.current_id is None:
            messagebox.showerror("Error", "Seleccione un proveedor para actualizar.")
            return

        name = self.name_entry.get().strip()
        surname = self.surname_entry.get().strip()
        phone = self.phone_entry.get().strip()
        address = self.address_entry.get().strip()

        if not name or not surname or not phone or not address:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")
            return

        self.suppliers[self.current_id] = {
            "name": name,
            "surname": surname,
            "phone": phone,
            "address": address
        }

        self.populate_table()
        self.clear_entries()
        messagebox.showinfo("Éxito", "¡Proveedor actualizado exitosamente!")

    def delete_supplier(self):
        if self.current_id is None:
            messagebox.showerror("Error", "Seleccione un proveedor para eliminar.")
            return

        confirm = messagebox.askyesno("Confirmar", "¿Está seguro de que desea eliminar este proveedor?")
        if confirm:
            del self.suppliers[self.current_id]
            self.populate_table()
            self.clear_entries()
            messagebox.showinfo("Éxito", "¡Proveedor eliminado exitosamente!")

=======
    # Método para actualizar un proveedor
    def update_supplier(self):
    # Cargar datos del producto seleccionado a los campos de entrada
      selected = self.suppliers_table.selection()
      if selected:
        values = self.suppliers_table.item(selected, 'values')# Verifica si hay un proveedor seleccionado
        if values:
            self.id_entry.configure(state="normal")# Cargar el ID del proveedor seleccionado disabled para evitar cambios
            self.id_entry.delete(0, 'end')
            self.id_entry.insert(0, values[0])
            self.name_entry.delete(0, 'end')
            self.name_entry.insert(0, values[1])
            self.nit_entry.delete(0, 'end')
            self.nit_entry.insert(0, values[2])
            self.phone_entry.delete(0, 'end')
            self.phone_entry.insert(0, values[3])
            self.address_entry.delete(0, 'end')
            self.address_entry.insert(0, values[4])
            self.city_entry.delete(0, 'end')
            self.city_entry.insert(0, values[5])
            self.current_id = selected  # Guardar cuál es el proveedor seleccionado
            self.id_entry.configure(state="normal")  # Cargar el ID del proveedor seleccionado normal para permitir cambios
      else:
        messagebox.showwarning("Selecciona", "Selecciona un producto de la tabla.")

    # Método para aplicar la actualización del proveedor
    def apply_supplier_update(self):  
      supplier_id = self.id_entry.get().strip()
      name = self.name_entry.get().strip()
      nit = self.nit_entry.get().strip()
      phone = self.phone_entry.get().strip()
      address = self.address_entry.get().strip()
      city = self.city_entry.get().strip()

      # Verifica si los campos están vacíos
      if not supplier_id or not name or not nit or not phone or not address or not city:
        messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")
        return

        # Verifica si el proveedor existe
      if supplier_id not in self.suppliers:
        messagebox.showerror("Error", "El proveedor no existe.")
        return

      # Actualizar la información del proveedor
      self.suppliers[supplier_id] = {
        "name": name,
        "nit": nit,
        "phone": phone,
        "address": address,
        "city": city
    }

      self.populate_table()
      self.clear_entries()
      self.id_entry.configure(state="normal")  # Por si quedó deshabilitado
      messagebox.showinfo("Éxito", "Proveedor actualizado correctamente.")

    # Método para eliminar un proveedor
    def delete_supplier(self):
        selected = self.suppliers_table.selection()
        if selected:  # Verifica si hay un proveedor seleccionado
            confirm = messagebox.askyesno("Confirmar eliminación", "¿Seguro que deseas eliminar el proveedor?")
            if confirm:
                supplier_id = self.suppliers_table.item(selected[0], "values")[0]
                del self.suppliers[supplier_id]
                self.populate_table()
                self.clear_entries()
                messagebox.showinfo("Éxito", "¡Proveedor eliminado exitosamente!")
        else:
            messagebox.showwarning("Selecciona", "Selecciona un proveedor en la tabla.")

     # Método para manejar la selección de un elemento en la tabla
>>>>>>> db887b8 (Actualizando interfaces de usuario colores y funciones)
    def on_item_selected(self, event):
        selected = self.suppliers_table.selection()
        if selected:
            item_data = self.suppliers_table.item(selected[0], "values")
            self.current_id = item_data[0]

            self.id_entry.configure(state="normal")
            self.id_entry.delete(0, "end")
            self.id_entry.insert(0, item_data[0])
            self.id_entry.configure(state="disabled")

            self.name_entry.delete(0, "end")
            self.name_entry.insert(0, item_data[1])
<<<<<<< HEAD
            self.surname_entry.delete(0, "end")
            self.surname_entry.insert(0, item_data[2])
=======
            self.nit_entry.delete(0, 'end')
            self.nit_entry.insert(0, item_data[2])
>>>>>>> db887b8 (Actualizando interfaces de usuario colores y funciones)
            self.phone_entry.delete(0, "end")
            self.phone_entry.insert(0, item_data[3])
            self.address_entry.delete(0, "end")
            self.address_entry.insert(0, item_data[4])
<<<<<<< HEAD

    def clear_entries(self):
        self.id_entry.configure(state="normal")
        self.id_entry.delete(0, "end")
        self.name_entry.delete(0, "end")
        self.surname_entry.delete(0, "end")
        self.phone_entry.delete(0, "end")
        self.address_entry.delete(0, "end")
        self.current_id = None

    def back_to_dashboard(self):
=======
            self.city_entry.delete(0, "end")
            self.city_entry.insert(0, item_data[5])

    def clear_entries(self):# Método para limpiar las entradas
        self.id_entry.configure(state="normal")
        self.id_entry.delete(0, "end")
        self.name_entry.delete(0, "end")
        self.nit_entry.delete(0, "end")
        self.phone_entry.delete(0, "end")
        self.address_entry.delete(0, "end")
        self.city_entry.delete(0, "end")
        self.current_id = None

    def back_to_dashboard(self):# Método para regresar al panel de control
>>>>>>> db887b8 (Actualizando interfaces de usuario colores y funciones)
        self.destroy()
        self.master.deiconify()


if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    root = ctk.CTk()
    root.withdraw()
    app = SuppliersApp(root)
    app.mainloop()
    root.destroy()