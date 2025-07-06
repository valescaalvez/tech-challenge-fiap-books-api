# Tech Challenge FIAP - API Pública de Livros

## Descrição do Projeto

Este projeto faz parte do Tech Challenge da Fase 1 do curso de Machine Learning Engineering da FIAP. O objetivo é construir um pipeline completo de dados, realizando web scraping no site [Books to Scrape](https://books.toscrape.com/), armazenando os dados localmente, e disponibilizando-os através de uma API pública RESTful, pronta para integração futura com soluções de Data Science e Machine Learning.

O projeto é composto por três grandes etapas:
1. **Web Scraping** dos livros do site Books to Scrape, salvando os dados em CSV.
2. **API RESTful** desenvolvida em Flask, expondo os dados do CSV.
3. **Deploy** da API em ambiente público.

---

## Arquitetura do Projeto

IMAGEM !!!!!


Web Scraper: Extrai os dados de livros do site e salva em data/books.csv.

API Flask: Lê o CSV e oferece endpoints RESTful para consulta, busca e análise dos livros.

Deploy: API acessível publicamente para cientistas de dados, integrações e consumidores externos.

## Instruções de Instalação e Configuração
Clone o repositório:

git clone https://github.com/seu-usuario/tech-challenge-fiap-books-api.git
cd tech-challenge-fiap-books-api
Crie e ative um ambiente virtual:

Windows:

```
python -m venv venv
venv\Scripts\activate
```
Linux/Mac:
```
python3 -m venv venv
source venv/bin/activate
Instale as dependências:
```

`pip install -r requirements.txt`
(Opcional) Gere o arquivo data/books.csv:


`python scripts/scrape_books.py`
O arquivo CSV já está disponível no repositório, mas pode ser atualizado rodando o script acima.

Documentação das Rotas da API
A documentação interativa completa (Swagger) está disponível em:

http://localhost:5000/apidocs

Principais endpoints:

Método	Endpoint	Descrição
GET	/api/v1/health	Verifica se a API está online  
GET	/api/v1/books	Lista todos os livros  
GET	/api/v1/books/<id>	Detalhes de um livro por ID  
GET	/api/v1/books/search?title=&category=	Busca livros por título/categoria  
GET	/api/v1/categories	Lista todas as categorias  

Exemplos de Chamadas
1. Listar todos os livros

GET /api/v1/books
Exemplo de resposta:


[
  {
    "id": 0,
    "titulo": "A Light in the ...",
    "preco": 51.77,
    "avaliacao": "Three",
    "estoque": "In stock (22 available)",
    "categoria": "Travel",
    "url_imagem": "https://books.toscrape.com/media/...",
    "url_livro": "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
  },
  ...
]
2. Detalhar um livro específico

GET /api/v1/books/0
Exemplo de resposta:

{
  "id": 0,
  "titulo": "A Light in the ...",
  "preco": 51.77,
  "avaliacao": "Three",
  "estoque": "In stock (22 available)",
  "categoria": "Travel",
  "url_imagem": "https://books.toscrape.com/media/...",
  "url_livro": "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
}
3. Buscar por título e categoria

GET /api/v1/books/search?title=light&category=travel
Exemplo de resposta:

[
  {
    "id": 0,
    "titulo": "A Light in the ...",
    "preco": 51.77,
    "avaliacao": "Three",
    "estoque": "In stock (22 available)",
    "categoria": "Travel",
    "url_imagem": "https://books.toscrape.com/media/...",
    "url_livro": "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
  }
]
4. Listar todas as categorias

GET /api/v1/categories
Exemplo de resposta:


["Travel", "Mystery", "Historical Fiction", ...]
5. Healthcheck

GET /api/v1/health
Exemplo de resposta:


{ "status": "ok" }
Instruções para Execução
Ative o ambiente virtual:
(Se não estiver ativo)

Execute a API:


python app.py
Acesse a documentação interativa:

http://localhost:5000/apidocs

Utilize ferramentas como Postman, Insomnia, curl ou navegador para testar os endpoints.

Observações Finais
O deploy público pode ser realizado em plataformas como Render, Heroku ou Fly.io.

Sinta-se à vontade para criar issues ou sugestões neste repositório!
