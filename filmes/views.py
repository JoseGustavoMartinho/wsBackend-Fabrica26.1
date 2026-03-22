from django.shortcuts import render, redirect, get_object_or_404
from .models import Categoria, Filme
from .forms import CategoriaForm, FilmeForm
import requests


def listar_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'filmes/categorias/lista.html', {'categorias': categorias})


def criar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_categorias')
    else:
        form = CategoriaForm()

    return render(request, 'filmes/categorias/form.html', {'form': form})


def editar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)

    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('listar_categorias')
    else:
        form = CategoriaForm(instance=categoria)

    return render(request, 'filmes/categorias/form.html', {'form': form})


def deletar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)

    if request.method == 'POST':
        categoria.delete()
        return redirect('listar_categorias')

    return render(request, 'filmes/categorias/confirmar_delete.html', {'categoria': categoria})

def listar_filmes(request):
    filmes = Filme.objects.all()
    return render(request, 'filmes/filmes/lista.html', {'filmes': filmes})


def criar_filme(request):
    if request.method == 'POST':
        form = FilmeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_filmes')
    else:
        form = FilmeForm()
        
    return render(request, 'filmes/filmes/form.html', {'form': form})



def editar_filme(request, pk):
    filme = get_object_or_404(Filme, pk=pk)

    if request.method == 'POST':
        form = FilmeForm(request.POST, instance=filme)
        if form.is_valid():
            form.save()
            return redirect('listar_filmes')
    else:
        form = FilmeForm(instance=filme)

    return render(request, 'filmes/filmes/form.html', {'form': form})

def deletar_filme(request, pk):
    filme = get_object_or_404(Filme, pk=pk)
    
    if request.method == 'POST':
        filme.delete()
        return redirect('listar_filmes')
    
    return render(request, 'filmes/filmes/confirmar_delete.html', {'filme': filme})


def buscar_filme_api(request):
    categorias = Categoria.objects.all()

    if request.method == 'POST':
        titulo = request.POST.get('titulo', '').strip()
        categoria_id = request.POST.get('categoria')

        url = f'https://www.omdbapi.com/?t={titulo}&apikey=69a9ee74'
        response = requests.get(url)
        data = response.json()

        if data.get('Response') == 'True':
            categoria = Categoria.objects.get(id=categoria_id)

            Filme.objects.create(
                titulo=data.get('Title', ''),
                ano=data.get('Year', ''),
                descricao=data.get('Plot', 'Descrição não disponível'),
                genero=data.get('Genre', ''),
                diretor=data.get('Director', ''),
                poster=data.get('Poster', ''),
                categoria=categoria
            )
            return redirect('listar_filmes')

        return render(request, 'filmes/filmes/buscar_api.html', {
            'categorias': categorias,
            'erro': 'Filme não encontrado na API'
        })

    return render(request, 'filmes/filmes/buscar_api.html', {'categorias': categorias})
# Create your views here.
