def test_overview_stats(test_client, auth_headers):
    response = test_client.get('/api/v1/stats/overview', headers=auth_headers)
    assert response.status_code == 200
    stats = response.json
    assert 'total_books' in stats
    assert 'average_price' in stats
    assert 'rating_distribution' in stats
    assert isinstance(stats['rating_distribution'], dict)

def test_category_stats(test_client, auth_headers):
    response = test_client.get('/api/v1/stats/categories', headers=auth_headers)
    assert response.status_code == 200
    categories = response.json
    assert isinstance(categories, dict)
    for category, stats in categories.items():
        assert 'count' in stats
        assert 'min_price' in stats
        assert 'max_price' in stats
        assert 'avg_price' in stats