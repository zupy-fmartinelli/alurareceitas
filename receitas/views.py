from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.
def index(request):
    # return HttpResponse('<h1>Receitas</h1> <h2>Bem Vindo</h2>')
    receitas = {
        1:'Lasanha',
        2:'Sopa de Legumes',
        3:'Sorvete',
        4:'Bolo de Chocolate'
    }
    dados = {
        'nome_das_receitas' : receitas
    }
    return render(request, 'index.html', dados)

def receita(request):
    return render(request, 'receita.html')
    