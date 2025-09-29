import os
import platform
import socket
from datetime import datetime

# Definición del archivo de log
LOG_FILE = "actividad.log"

# Definición de funciones para manejar el registro de actividades de usuarios
def registrar_actividad(usuario, tipo_usuario, accion):
    """Registra una línea de actividad en el archivo log."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ip_local = socket.gethostbyname(socket.gethostname())
    sistema = platform.system()
    linea = f"[{timestamp}] Usuario: {usuario} ({tipo_usuario}) | IP: {ip_local} | SO: {sistema} | Acción: {accion}\n"

    # Registrar la actividad en el archivo log
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(linea)

# Funciones para leer y filtrar actividades
def leer_actividades(ultimas_n=None):
    """Lee las actividades del log; si ultimas_n se da, devuelve solo las últimas N líneas."""
    if not os.path.exists(LOG_FILE):
        return []

    with open(LOG_FILE, "r", encoding="utf-8") as f:
        lineas = f.readlines()

    if ultimas_n:
        return lineas[-ultimas_n:]
    return lineas

# Funciones para limpiar y filtrar actividades
def limpiar_log():
    """Limpia el archivo de log (cuidado: elimina todo)."""
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        f.truncate(0)

# Funciones para filtrar actividades
def filtrar_actividades_por_usuario(usuario):
    """Devuelve las líneas del log para un usuario específico."""
    actividades = leer_actividades()
    return [linea for linea in actividades if f"Usuario: {usuario}" in linea]
    

# Función para filtrar actividades por tipo de usuario
def filtrar_actividades_por_tipo(tipo_usuario):
    """Devuelve las líneas del log para un tipo de usuario (admin/usuario)."""
    actividades = leer_actividades()
    return [linea for linea in actividades if f"({tipo_usuario})" in linea]

# Función para filtrar actividades por acción
def filtrar_actividades_por_accion(accion):
    """Devuelve las líneas del log que contienen una acción específica."""
    actividades = leer_actividades()
    return [linea for linea in actividades if f"Acción: {accion}" in linea]