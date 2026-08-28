from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *
from django.contrib import admin
admin.site.register(Cidade)

admin.site.register(editora)
admin.site.register(leitor)

admin.site.register(Genero)


class LivroInline(admin.TabularInline):
    model = livro
    extra = 1 # Número de livros adicionais para adicionar no admin


class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome',)# Campos que serão exibidos na listagem
    search_fields = ('nome',)# Campos que serão 
    inlines = [LivroInline]# Adiciona a tabela de livros no admin de gêneros


admin.site.register(Autor,AutorAdmin)
