def test_ml_features(test_client, auth_headers):
    response = test_client.get('/api/v1/ml/features', headers=auth_headers)
    assert response.status_code == 200
    features = response.json
    assert isinstance(features, list)
    for item in features:
        assert 'id' in item
        assert 'title' in item
        assert 'price' in item
        assert 'rating' in item
        assert 'category' in item
        assert 'availability' in item

def test_ml_training_data(test_client, auth_headers):
    response = test_client.get('/api/v1/ml/training-data', headers=auth_headers)
    assert response.status_code == 200
    training_data = response.json
    assert isinstance(training_data, list)
    for item in training_data:
        assert 'id' in item
        assert 'features' in item
        assert 'target' in item

def test_ml_predictions(test_client, auth_headers):
    sample_data = [
        {
            "book_id": 1,
            "features": {"rating": 4, "price": 15.99}
        },
        {
            "book_id": 2,
            "features": {"rating": 2, "price": 9.99}
        }
    ]
    
    response = test_client.post(
        '/api/v1/ml/predictions',
        json=sample_data,
        headers=auth_headers
    )
    assert response.status_code == 200
    predictions = response.json
    assert isinstance(predictions, list)
    assert len(predictions) == len(sample_data)
    for prediction in predictions:
        assert 'book_id' in prediction
        assert 'prediction' in prediction
        assert 'confidence' in prediction