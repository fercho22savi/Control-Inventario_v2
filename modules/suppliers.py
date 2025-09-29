import customtkinter as ctk
from tkinter import messagebox
from tkinter import ttk

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
        super().__init__(master)
        self.master = master
        self.title("Gestión de Proveedores")
        self.geometry("900x600")
        self.configure(fg_color=PALETA["fondo"])
        self.wm_attributes("-alpha", 0.85)

        self.suppliers = {}  # Diccionario para almacenar los proveedores
        self.current_id = None  # ID del proveedor actualmente seleccionado

        # Estilo oscuro para la tabla
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview",
                        background=PALETA["panel"],
                        foreground=PALETA["texto"],
                        fieldbackground=PALETA["panel"],
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

    # Método para crear entradas con etiquetas
    def create_labeled_entry(self, parent, text, row):
        label = ctk.CTkLabel(parent, text=text, text_color="white")
        label.grid(row=row, column=0, sticky="w", padx=10, pady=8)
        entry = ctk.CTkEntry(parent, width=300)
        entry.grid(row=row, column=1, pady=8)
        return entry

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

    # Método para llenar la tabla con los datos de los proveedores
    def populate_table(self):
        for row in self.suppliers_table.get_children():
            self.suppliers_table.delete(row)
        for supplier_id, data in self.suppliers.items():
            self.suppliers_table.insert("", "end", values=(supplier_id, data["name"], data["nit"], data["phone"], data["address"], data["city"]))

    # Método para agregar un nuevo proveedor
    def add_supplier(self):
        supplier_id = self.id_entry.get().strip()
        name = self.name_entry.get().strip()
        nit = self.nit_entry.get().strip()
        phone = self.phone_entry.get().strip()
        address = self.address_entry.get().strip()
        city = self.city_entry.get().strip()

        if supplier_id in self.suppliers:
            messagebox.showerror("Error", "El ID ya existe.")
            return

        if not supplier_id or not name or not nit or not phone or not address or not city:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")
            return

        self.suppliers[supplier_id] = {"name": name, "nit": nit, "phone": phone, "address": address, "city": city}
        self.populate_table()
        self.clear_entries()
        messagebox.showinfo("Éxito", "¡Proveedor agregado exitosamente!")

    # Método para actualizar un proveedor (cargar datos al formulario)
    def update_supplier(self):
        selected = self.suppliers_table.selection()
        if selected:
            values = self.suppliers_table.item(selected[0], 'values')
            if values:
                self.id_entry.configure(state="normal")
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
                self.current_id = values[0]
                self.id_entry.configure(state="normal")
        else:
            messagebox.showwarning("Selecciona", "Selecciona un proveedor de la tabla.")

    # Aplicar actualización del proveedor
    def apply_supplier_update(self):
        supplier_id = self.id_entry.get().strip()
        name = self.name_entry.get().strip()
        nit = self.nit_entry.get().strip()
        phone = self.phone_entry.get().strip()
        address = self.address_entry.get().strip()
        city = self.city_entry.get().strip()

        if not supplier_id or not name or not nit or not phone or not address or not city:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")
            return

        if supplier_id not in self.suppliers:
            messagebox.showerror("Error", "El proveedor no existe.")
            return

        self.suppliers[supplier_id] = {"name": name, "nit": nit, "phone": phone, "address": address, "city": city}
        self.populate_table()
        self.clear_entries()
        messagebox.showinfo("Éxito", "Proveedor actualizado correctamente.")

    # Método para eliminar un proveedor
    def delete_supplier(self):
        selected = self.suppliers_table.selection()
        if selected:
            confirm = messagebox.askyesno("Confirmar eliminación", "¿Seguro que deseas eliminar el proveedor?")
            if confirm:
                supplier_id = self.suppliers_table.item(selected[0], "values")[0]
                del self.suppliers[supplier_id]
                self.populate_table()
                self.clear_entries()
                messagebox.showinfo("Éxito", "¡Proveedor eliminado exitosamente!")
        else:
            messagebox.showwarning("Selecciona", "Selecciona un proveedor en la tabla.")

    # Manejar selección en la tabla
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
            self.nit_entry.delete(0, "end")
            self.nit_entry.insert(0, item_data[2])
            self.phone_entry.delete(0, "end")
            self.phone_entry.insert(0, item_data[3])
            self.address_entry.delete(0, "end")
            self.address_entry.insert(0, item_data[4])
            self.city_entry.delete(0, "end")
            self.city_entry.insert(0, item_data[5])

    # Limpiar entradas
    def clear_entries(self):
        self.id_entry.configure(state="normal")
        self.id_entry.delete(0, "end")
        self.name_entry.delete(0, "end")
        self.nit_entry.delete(0, "end")
        self.phone_entry.delete(0, "end")
        self.address_entry.delete(0, "end")
        self.city_entry.delete(0, "end")
        self.current_id = None

    # Regresar al dashboard
    def back_to_dashboard(self):
        if self.master:
            self.master.deiconify()
        self.destroy()


if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    root = ctk.CTk()
    root.withdraw()  # Ocultar la ventana raíz
    app = SuppliersApp(root)
    app.mainloop()
    

