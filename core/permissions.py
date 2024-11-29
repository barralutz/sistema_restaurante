# core/permissions.py
from rest_framework.permissions import BasePermission

# Permiso personalizado para Meseros
class IsMesero(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Mesero').exists()

# Permiso personalizado para Cocina
class IsCocina(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Cocina').exists()

# Permiso personalizado para Parrilla
class IsParrilla(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Parrilla').exists()

# Permiso personalizado para Barra
class IsBarra(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Barra').exists()

# Permiso personalizado para Caja
class IsCaja(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Caja').exists()

# Permiso personalizado para Administrador
class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Administrador').exists()
