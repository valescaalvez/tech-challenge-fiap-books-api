def test_get_all_books(test_client, auth_headers):
    response = test_client.get('/api/v1/books', headers=auth_headers)
    assert response.status_code == 200
    assert isinstance(response.json, list)
    assert len(response.json) > 0

def test_get_single_book(test_client, auth_headers):
    response = test_client.get('/api/v1/books/0', headers=auth_headers)
    assert response.status_code == 200
    assert 'title' in response.json
    assert 'price' in response.json

def test_search_books(test_client, auth_headers):
    response = test_client.get(
        '/api/v1/books/search?title=python&category=programming',
        headers=auth_headers
    )
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_top_rated_books(test_client, auth_headers):
    response = test_client.get('/api/v1/books/top-rated', headers=auth_headers)
    assert response.status_code == 200
    assert isinstance(response.json, list)
    
    ratings = [book['rating'] for book in response.json]
    assert ratings == sorted(ratings, reverse=True)

def test_price_range_books(test_client, auth_headers):
    response = test_client.get(
        '/api/v1/books/price-range?min=10&max=20',
        headers=auth_headers
    )
    assert response.status_code == 200
    assert isinstance(response.json, list)
    
    for book in response.json:
        price = float(book['price'].replace('£', ''))
        assert 10 <= price <= 20