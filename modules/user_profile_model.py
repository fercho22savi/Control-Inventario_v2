# -*- coding: utf-8 -*-
# Modelo de datos para el usuario

# Clase que representa el perfil de un usuario
class UserProfile:
    def __init__(self, username, email, full_name, age, is_active=True):
        self.username = username
        self.email = email
        self.full_name = full_name
        self.age = age
        self.is_active = is_active  # Estado del usuario
        
   
    def __str__(self):
        return f"{self.full_name} ({self.username}) - {self.email}, Age: {self.age}, Active: {self.is_active}"
