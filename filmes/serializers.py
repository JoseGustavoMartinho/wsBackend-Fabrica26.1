from rest_framework import serializers
from .models import Filme, Categoria


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nome']


class FilmeSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer(read_only=True)

    class Meta:
        model = Filme
        fields = ['id', 'titulo', 'descricao', 'ano', 'genero', 'diretor', 'poster', 'categoria']