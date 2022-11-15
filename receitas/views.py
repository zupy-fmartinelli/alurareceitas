from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Receita #importa os modelos que estão nas classes

#from django.http import HttpResponse
# Create your views here.

def index(request):
    # return HttpResponse('<h1>Receitas</h1> <h2>Bem Vindo</h2>')

    # traz todos os objetos do banco de dados
    receitas = Receita.objects.order_by('-date_receita').filter(publicada=True)
    
    dados = {
        'receitas' : receitas
    }
    return render(request, 'receitas/index.html', dados)

def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    
    receita_a_exibir = {
        'receita' : receita
    }
    
    
    return render(request, 'receitas/receita.html', receita_a_exibir)

def buscar(request):
    lista_receitas = Receita.objects.order_by('-date_receita').filter(publicada=True)
    
    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if buscar:
            lista_receitas = lista_receitas.filter(nome_receita__icontains = nome_a_buscar)
            
    dados = {
        'receitas' : lista_receitas
    }            
    
    return render(request, 'receitas/buscar.html', dados)