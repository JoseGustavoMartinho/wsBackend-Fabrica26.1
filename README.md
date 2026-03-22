# wsBackend-Fabrica26.1

Sistema web desenvolvido com Django para gerenciamento de filmes e categorias, com cadastro manual e integração com a API OMDb.

## Funcionalidades

- CRUD completo de filmes
- CRUD completo de categorias
- Relacionamento entre filme e categoria
- Busca de filmes pela API OMDb
- Interface web com Django Templates
- Estilização com CSS próprio

## Tecnologias utilizadas

- Python 3.11
- Django 5.2
- HTML
- CSS
- Requests
- SQLite (execução local)

## Rotas principais

### Web
- /filmes/
- /filmes/criar/
- /filmes/buscar-api/
- /categorias/

## Como executar o projeto

1. Instale as dependências:

pip install -r requirements.txt


2. Execute as migrations:

python manage.py migrate


3. Inicie o servidor:

python manage.py runserver


4. Acesse no navegador:

http://127.0.0.1:8000/filmes/


## Autor

José Gustavo Martinho