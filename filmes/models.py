from django.db import models

# Categoria do filme
class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


# Filme
class Filme(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    ano = models.IntegerField()

    genero = models.CharField(max_length=100, blank=True, null=True)
    diretor = models.CharField(max_length=100, blank=True, null=True)
    poster = models.URLField(blank=True, null=True)

    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo