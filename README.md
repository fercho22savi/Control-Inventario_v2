# 📦 Sistema de Control de Inventario (Python & SQLite)

Este repositorio contiene un sistema integral de gestión de inventario con una interfaz gráfica (GUI) moderna, desarrollado en **Python** utilizando la librería `CustomTkinter`. 

El sistema permite administrar de forma centralizada **clientes**, **proveedores** y **productos** a través de un panel de control inteligente.

---

## 🎯 Funcionalidades Principales

*   🔐 **Login de Acceso:** Sistema de seguridad con gestión de 3 tipos de roles de usuario.
*   📊 **Dashboard Moderno:** Interfaz con diseño oscuro, efectos de transparencia y navegación intuitiva.
*   📦 **Gestión de Módulos:**
    *   **Clientes:** Control detallado de base de datos de clientes.
    *   **Proveedores:** Administración de cadena de suministro.
    *   **Productos:** Control de stock y catálogos.
*   🔄 **Navegación Fluida:** Transiciones dinámicas entre módulos sin abrir múltiples ventanas.
*   📂 **Persistencia de Datos:** Integración completa con **SQLite** para almacenamiento local ligero y eficiente.

---

## 🖥️ Tecnologías Utilizadas

*   **Lenguaje:** Python 3.x
*   **GUI:** [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) (Evolución moderna de Tkinter).
*   **Base de Datos:** SQLite.
*   **Visualización:** Matplotlib & Mpl_toolkits (Gráficos 2D y 3D).
*   **Procesamiento:** Numpy.
*   **Imágenes:** Pillow (PIL).

---

## ⚙️ Instalación y Requisitos

Para ejecutar este proyecto, asegúrate de tener instaladas las siguientes dependencias:

```bash
# Instalación de la interfaz gráfica moderna
pip install customtkinter

# Librería para manejo de imágenes
pip install pillow

# Manejo de variables de entorno
pip install python-dotenv

# Procesamiento de datos y gráficos
pip install numpy matplotlib
```

---

## 🧠 Sobre la Arquitectura del Código

El sistema sigue una lógica modular para facilitar el mantenimiento. El archivo central es `dashboard.py`, que gestiona la clase principal `Dashboard`.

### Flujo de Navegación:
Cuando el usuario interactúa con el menú lateral, el sistema oculta el panel actual y llama a las clases específicas sin cerrar la aplicación principal:
*   `SuppliersApp`: Módulo de proveedores.
*   `ClientsApp`: Módulo de clientes.
*   `ProductApp`: Módulo de productos.
*   `UserActivityDashboard`: Monitoreo de actividad y logs.

### Estructura de Clases Internas:
*   **registro / administrador:** Gestión de permisos y nuevos usuarios.
*   **user_info / user_Profile_model:** Manejo de perfiles y datos del usuario actual.
*   **log_manager:** Registro de eventos del sistema para auditoría.

---

## 📌 Notas de Diseño

Para garantizar una experiencia visual "Premium", el sistema está configurado por defecto con:
*   **Apariencia:** `set_appearance_mode("dark")`
*   **Tema de color:** `set_default_color_theme("dark-blue")`

---

## ✍️ Autor
**Fernando Saldaña**  
*Desarrollador de Software*

---

⭐ **¿Te gusta este proyecto?** ¡Dale una estrella al repositorio y compártelo!
