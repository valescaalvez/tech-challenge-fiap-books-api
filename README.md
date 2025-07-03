# Tech Challenge FIAP - API Pública de Livros

## Descrição do Projeto

Este projeto faz parte do Tech Challenge da Fase 1 do curso de Machine Learning Engineering da FIAP. O objetivo é construir um pipeline completo de dados, realizando web scraping no site [Books to Scrape](https://books.toscrape.com/), armazenando os dados localmente, e disponibilizando-os através de uma API pública RESTful, pronta para integração futura com soluções de Data Science e Machine Learning.

O projeto é composto por três grandes etapas:
1. **Web Scraping** dos livros do site Books to Scrape, salvando os dados em CSV.
2. **API RESTful** desenvolvida em Flask, expondo os dados do CSV.
3. **Deploy** da API em ambiente público.

---

## Arquitetura do Projeto

------------------------------------------------------------


Web Scraper: Extrai os dados de livros do site e salva em data/books.csv.

API Flask: Lê o CSV e oferece endpoints RESTful para consulta, busca e análise dos livros.

Deploy: API acessível publicamente para cientistas de dados, integrações e consumidores externos.

