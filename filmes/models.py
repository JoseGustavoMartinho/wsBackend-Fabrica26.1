from django.db import models

# ==============================
# Model de Categoria
# ==============================
# Representa os tipos de filmes (Ação, Comédia, etc)
class Categoria(models.Model):
    # Nome da categoria
    nome = models.CharField(max_length=100)

    def __str__(self):
        # Retorna o nome da categoria
        return self.nome


# ==============================
# Model de Filme
# ==============================
# Representa um filme cadastrado no sistema
class Filme(models.Model):
    # Título do filme
    titulo = models.CharField(max_length=200)

    # Descrição / sinopse
    descricao = models.TextField()

    # Ano de lançamento
    ano = models.IntegerField()

    # Gênero do filme (opcional)
    genero = models.CharField(max_length=100, blank=True, null=True)

    # Diretor do filme (opcional)
    diretor = models.CharField(max_length=100, blank=True, null=True)

    # URL da imagem do poster (opcional)
    poster = models.URLField(blank=True, null=True)

    # Relação com categoria (chave estrangeira)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        # Retorna o título do filme
        return self.titulo
# Create your models here.
