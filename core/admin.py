# core/admin.py
from django.contrib import admin
from .models import Area, Platillo, Pedido, Parte

admin.site.register(Area)
admin.site.register(Platillo)
admin.site.register(Pedido)
admin.site.register(Parte)
