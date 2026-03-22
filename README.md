# wsBackend-Fabrica26.1

Projeto desenvolvido em Django para o desafio da Fábrica de Software.

O sistema permite cadastrar, editar, listar e remover categorias e filmes.  
Além disso, também consome uma API externa gratuita (OMDb API) para buscar informações de filmes e salvar no banco de dados.

---

## Funcionalidades

- CRUD completo de Categorias
- CRUD completo de Filmes
- Relacionamento entre Filme e Categoria
- Busca de filmes por API externa
- Salvamento das informações no banco de dados
- Interface web com Django Templates

---

## Tecnologias utilizadas

- Python
- Django
- SQLite
- HTML
- Requests

---

## Estrutura do projeto

- `Categoria`: entidade responsável por classificar os filmes
- `Filme`: entidade principal do sistema, ligada a uma categoria
- API externa: OMDb API

---

## Banco de dados

O projeto utiliza **SQLite** como banco de dados padrão do Django.

As informações cadastradas manualmente ou vindas da API são armazenadas no arquivo local do banco.

Exemplos de dados salvos:
- nome da categoria
- título do filme
- descrição
- ano
- categoria relacionada

---

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/SEU-USUARIO/wsBackend-Fabrica26.1.git
cd wsBackend-Fabrica26.1