from django import forms
from .models import Categoria, Filme

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']
        
class FilmeForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = ['titulo', 'descricao', 'ano', 'categoria']