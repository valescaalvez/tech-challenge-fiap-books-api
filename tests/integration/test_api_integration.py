def test_full_workflow(test_client):
    login_response = test_client.post('/api/v1/auth/login', json={
        'username': 'admin',
        'password': 'senha'
    })
    assert login_response.status_code == 200
    access_token = login_response.json['access_token']
    headers = {'Authorization': f'Bearer {access_token}'}
    
    books_response = test_client.get('/api/v1/books', headers=headers)
    assert books_response.status_code == 200
    books = books_response.json
    assert len(books) > 0
    
    book_id = books[0]['id']
    book_response = test_client.get(f'/api/v1/books/{book_id}', headers=headers)
    assert book_response.status_code == 200
    
    stats_response = test_client.get('/api/v1/stats/overview', headers=headers)
    assert stats_response.status_code == 200
    
    features_response = test_client.get('/api/v1/ml/features', headers=headers)
    assert features_response.status_code == 200
    
    sample_book = features_response.json[0]
    prediction_data = [{
        "book_id": sample_book['id'],
        "features": {
            "rating": sample_book['rating'],
            "price": sample_book['price']
        }
    }]
    
    prediction_response = test_client.post(
        '/api/v1/ml/predictions',
        json=prediction_data,
        headers=headers
    )
    assert prediction_response.status_code == 200