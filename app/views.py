import json
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
    def post(self, request):
        pass

class LivrosView(View):
    def get(self, request, *args, **kwargs):
        livros = livro.objects.all()
        return render(request, 'livros.html', {'livros': livros})

class CidadesView(View):
    def get(self, request, *args, **kwargs):
        cidades = Cidade.objects.all()
        return render(request, 'cidade.html', {'cidades': cidades})

class AutoresView(View):
    def get(self, request, *args, **kwargs):
        autores = Autor.objects.all()
        return render(request, 'autor.html', {'autores': autores})

class EditorasView(View):
    def get(self, request, *args, **kwargs):
        editoras = editora.objects.all()
        return render(request, 'editora.html', {'editoras': editoras})

class LeitoresView(View):
    def get(self, request, *args, **kwargs):
        leitores = leitor.objects.all()
        return render(request, 'leitor.html', {'leitores': leitores})

class GenerosView(View):
    def get(self, request, *args, **kwargs):
        generos = Genero.objects.all()
        return render(request, 'genero.html', {'generos': generos})

@csrf_exempt
def api_criar_leitor(request):
    if request.method == 'POST':
        try:
            dados = json.loads(request.body)
            leitor.objects.create(
                nome=dados.get('nome', ''),
                email=dados.get('email', ''),
                cpf=dados.get('cpf', '')
            )
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'status': 'invalid method'}, status=405)