from django.urls import path
from . import views

urlpatterns = [
    path('categorias/', views.listar_categorias, name='listar_categorias'),
    path('categorias/criar/', views.criar_categoria, name='criar_categoria'),
    path('categorias/<int:pk>/editar/', views.editar_categoria, name='editar_categoria'),
    path('categorias/<int:pk>/deletar/', views.deletar_categoria, name='deletar_categoria'),
    
    path('filmes/', views.listar_filmes, name='listar_filmes'),
    path('filmes/criar/', views.criar_filme, name='criar_filme'),
    path('filmes/<int:pk>/editar/', views.editar_filme, name='editar_filme'),
    path('filmes/<int:pk>/deletar/', views.deletar_filme, name='deletar_filme'),
      
]