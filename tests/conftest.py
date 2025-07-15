import sys
import os
import pytest
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))

from api import create_app

@pytest.fixture(scope='module')
def test_client():
    os.environ['DATA_PATH'] = str(ROOT_DIR / 'data' / 'processed' / 'books.csv')
    os.environ['JWT_SECRET_KEY'] = 'test_secret'
    
    flask_app = create_app()
    flask_app.config['TESTING'] = True
    
    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            yield testing_client

@pytest.fixture(scope='module')
def auth_headers(test_client):
    response = test_client.post('/api/v1/auth/login', json={
        'username': 'admin',
        'password': 'senha'
    })
    access_token = response.json['access_token']
    return {'Authorization': f'Bearer {access_token}'}