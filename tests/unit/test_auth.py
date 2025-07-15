def test_login_success(test_client):
    response = test_client.post('/api/v1/auth/login', json={
        'username': 'admin',
        'password': 'senha'
    })
    assert response.status_code == 200
    assert 'access_token' in response.json
    assert 'refresh_token' in response.json

def test_login_failure(test_client):
    response = test_client.post('/api/v1/auth/login', json={
        'username': 'wrong',
        'password': 'wrong'
    })
    assert response.status_code == 401
    assert response.json['msg'] == "Usuário ou senha inválidos"

def test_token_refresh(test_client, auth_headers):
    login_response = test_client.post('/api/v1/auth/login', json={
        'username': 'admin',
        'password': 'senha'
    })
    refresh_token = login_response.json['refresh_token']
    
    response = test_client.post('/api/v1/auth/refresh', headers={
        'Authorization': f'Bearer {refresh_token}'
    })
    assert response.status_code == 200
    assert 'access_token' in response.json