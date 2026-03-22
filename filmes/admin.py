from django.contrib import admin
from .models import Categoria, Filme

# Registra os models no painel administrativo
admin.site.register(Categoria)
admin.site.register(Filme)