# 📦 Sistema de Control de Inventario

Este repositorio contiene un sistema de gestión de inventario con interfaz gráfica, desarrollado en Python utilizando `CustomTkinter`. El sistema está diseñado para administrar **clientes**, **proveedores** y **productos** desde un panel central o _dashboard_.

---

## 🎯 Funcionalidades
_ ** Login
- **Dashboard moderno** con diseño oscuro y transparente.(Administra tres tipos de usuario)
- Módulo de **Clientes**.
- Módulo de **Proveedores**.
- Módulo de **Productos**.
- Navegación fluida entre módulos.
- Botones de funciones y salida para cerrar la aplicación.
- Base de datos sqLITE

---

## 🖥️ Tecnologías utilizadas

- Python 3
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) (para una interfaz moderna y personalizable)
- Estructura modular
- Base de datos sqLITE

---

## 📁 Estructura del proyecto

## Requisitos:
## Instala los requisitos (si no tienes CustomTkinter):

pip install customtkinter (Interfaz grafica python)
pip3 install pillow (Libreria python para trabajar con imagenes)
pip install python-dotenv (Entorno virtual)
pip install numpy (Manejo de arrays y matrices)
pip install matplotlib (libreria para genera graficos y visualizaciones de datos)
mpl_toolkits.mplot3d (herramienta integrada a matplotlib para 3d)

🧠 Sobre el código
El archivo dashboard.py contiene la clase principal Dashboard, 
que representa la ventana principal con botones para abrir cada uno de los módulos del sistema. 
Cada botón llama a una clase distinta para manejar las operaciones específicas:

SuppliersApp para proveedores.
ClientsApp para clientes.
ProductApp para productos.
registro.
administrador
user_info
user_Profile_model
log_manager
UserActivityDashboard
dashboard



Al hacer clic en un botón, se oculta el dashboard actual y se muestra el módulo correspondiente,
 permitiendo al usuario trabajar de forma específica y luego regresar al panel general.

📌 Notas adicionales
El sistema utiliza set_appearance_mode("dark") y set_default_color_theme("dark-blue") para una experiencia visual moderna.

Los módulos deben ser desarrollados y mantenidos en sus archivos correspondientes para asegurar una buena organización.

✍️ Autor
Fernando saldaña
Desarrollador 


