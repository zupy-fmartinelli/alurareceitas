from django.shortcuts import render
from .models import Receita #importa os modelos que estão nas classes

#from django.http import HttpResponse
# Create your views here.

def index(request):
    # return HttpResponse('<h1>Receitas</h1> <h2>Bem Vindo</h2>')

    # traz todos os objetos do banco de dados
    receitas = Receita.objects.all()
    
    dados = {
        'receitas' : receitas
    }
    return render(request, 'index.html', dados)

def receita(request):
    return render(request, 'receita.html')
    