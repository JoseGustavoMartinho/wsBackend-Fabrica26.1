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
- SQLite (para desenvolvimento local)

## Estrutura principal

- `Filme`: entidade principal do sistema
- `Categoria`: classificação dos filmes
- `OMDb API`: busca de informações externas

## Banco de dados

O projeto utiliza SQLite para facilitar a execução local.

As informações cadastradas manualmente ou vindas da API são persistidas no banco, incluindo:

- título
- descrição
- ano
- gênero
- diretor
- poster
- categoria relacionada

## Rotas principais

### Web
- `/filmes/`
- `/filmes/criar/`
- `/filmes/buscar-api/`
- `/categorias/`

## Como executar o projeto

### 1. Clonar o repositório
```bash
git clone https://github.com/JoseGustavoMartinho/wsBackend-Fabrica26.1.git
cd wsBackend-Fabrica26.1