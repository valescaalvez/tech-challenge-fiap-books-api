<<<<<<< HEAD
Como Executar o Projeto Localmente
1. Clone o repositório

git clone https://github.com/seu-usuario/seu-repositorio.git
cd tech-challenge-fiap-books-api-main

2. Crie e ative o ambiente virtual

python -m venv venv
# No Windows PowerShell
.\venv\Scripts\Activate.ps1
# Ou no CMD:
venv\Scripts\activate

3. Instale as dependências

pip install -r requirements.txt

4. Extraia os dados dos livros

python scripts/process_data.py

Isso vai criar o arquivo data/books.csv com todos os livros do site.

5. Execute a API

uvicorn api.main:app --reload

Acesse em: http://localhost:8000/docs para testar.

- Endpoints já implementados
GET /api/v1/books
Lista todos os livros disponíveis na base.

# O que falta implementar

- Endpoints: detalhes por ID, busca por título/categoria, categorias, health.

- Testes automáticos.

- Documentação final do projeto.

- Deploy em ambiente público (Heroku, Render, etc).

- Vídeo de apresentação (conforme desafio).

## Equipe

[Felipe Breseghello](https://github.com/fbreseghello)

[Valesca Alvez](https://github.com/valescaalvez)

[Brunno Salvatti](https://github.com/brunnosalvatti)

...


## Referências
books.toscrape.com

Documentação FastAPI
=======
# tech-challenge-fiap-books-api
>>>>>>> efa5df89fdabc6d250c8e1ac5408dcf4bfc27fd8
