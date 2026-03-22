from django.shortcuts import render, redirect, get_object_or_404
from .models import Categoria, Filme
from .forms import CategoriaForm, FilmeForm
import requests

# ==============================
# FILMES
# ==============================

# Lista todos os filmes cadastrados
def listar_filmes(request):
    filmes = Filme.objects.all()
    return render(request, 'filmes/lista.html', {'filmes': filmes})


# Cria um novo filme manualmente
def criar_filme(request):
    categorias = Categoria.objects.all()

    if request.method == 'POST':
        form = FilmeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_filmes')
    else:
        form = FilmeForm()

    return render(request, 'filmes/form.html', {'form': form})


# Edita um filme existente
def editar_filme(request, pk):
    filme = get_object_or_404(Filme, pk=pk)

    if request.method == 'POST':
        form = FilmeForm(request.POST, instance=filme)
        if form.is_valid():
            form.save()
            return redirect('listar_filmes')
    else:
        form = FilmeForm(instance=filme)

    return render(request, 'filmes/form.html', {'form': form})


# Deleta um filme
def deletar_filme(request, pk):
    filme = get_object_or_404(Filme, pk=pk)

    if request.method == 'POST':
        filme.delete()
        return redirect('listar_filmes')

    return render(request, 'filmes/confirmar_delete.html', {'filme': filme})


# Busca filme na API OMDb e salva no banco
def buscar_filme_api(request):
    categorias = Categoria.objects.all()

    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        categoria_id = request.POST.get('categoria')

        # Requisição para API externa
        url = f'https://www.omdbapi.com/?t={titulo}&apikey=69a9ee74'
        response = requests.get(url)
        data = response.json()

        # Verifica se encontrou o filme
        if data.get('Response') == 'True':
            categoria = Categoria.objects.get(id=categoria_id)

            # Cria o filme com dados da API
            Filme.objects.create(
                titulo=data.get('Title'),
                ano=data.get('Year'),
                descricao=data.get('Plot'),
                genero=data.get('Genre'),
                diretor=data.get('Director'),
                poster=data.get('Poster'),
                categoria=categoria
            )
            return redirect('listar_filmes')

    return render(request, 'filmes/buscar_api.html', {'categorias': categorias})


# ==============================
# CATEGORIAS
# ==============================

# Lista categorias
def listar_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'filmes/categorias/lista.html', {'categorias': categorias})


# Cria categoria
def criar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_categorias')
    else:
        form = CategoriaForm()

    return render(request, 'filmes/categorias/form.html', {'form': form})


# Edita categoria
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


# Deleta categoria
def deletar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)

    if request.method == 'POST':
        categoria.delete()
        return redirect('listar_categorias')

    return render(request, 'filmes/categorias/confirmar_delete.html', {'categoria': categoria})