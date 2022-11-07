from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Receita #importa os modelos que estão nas classes

#from django.http import HttpResponse
# Create your views here.

def index(request):
    # return HttpResponse('<h1>Receitas</h1> <h2>Bem Vindo</h2>')

    # traz todos os objetos do banco de dados
    receitas = Receita.objects.filter(publicada=True)
    
    dados = {
        'receitas' : receitas
    }
    return render(request, 'index.html', dados)

def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    
    receita_a_exibir = {
        'receita' : receita
    }
    
    
    return render(request, 'receita.html', receita_a_exibir)

    