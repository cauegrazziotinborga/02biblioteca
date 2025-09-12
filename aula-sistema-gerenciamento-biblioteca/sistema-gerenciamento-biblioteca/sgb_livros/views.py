from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Livro

# Create your views here.
def livros(request):
    #return HttpResponse('Olá mundo')
    return render(request, 'livros.html')

def salva_livros(request):
    titulo_livro = request.POST['titulo_livro']
    autor_livro = request.POST['autor_livro']
    editora_livro = request.POST['editora_livro']
    return render(request, 'livros.html', context = {'titulo_livro': titulo_livro})
    #return HttpResponse('Livro salvo!' + titulo_livro)

def cadastra_livro(request):
    if request.method == 'POST':
        livro_id = request.POST['livro_id']
        titulo = request.POST['titulo']
        autor = request.POST['autor']
        ano_publicacao = request.POST['ano_publicacao']
        editora = request.POST['editora']

        if livro_id:        # Edita livro
            livro = livro_id
            livro.titulo = titulo
            livro.autor = autor
            livro.ano_publicacao = ano_publicacao
            livro.editora = editora
            livro.save()
        else:       # Salva um novo livro
            Livro.objects.create(
                titulo = titulo,
                autor = autor,
                ano_publicacao = ano_publicacao,
                editora = editora
            )
        return redirect('cadastra_livro')
    # objects é o gerenciador do Django que serve para consultar o banco.
    # all() é uma função que retorna todos os registros da tabela livro. (mesma coisa que o SELECT em Banco de Dados).
    livros = Livro.objects.all()
    return render(request, 'livros.html', {'livros': livros})
