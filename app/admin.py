from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *
from django.contrib import admin
admin.site.register(Cidade)
admin.site.register(Autor)
admin.site.register(editora)
admin.site.register(leitor)
admin.site.register(livro)
admin.site.register(Genero)
