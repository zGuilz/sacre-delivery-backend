def test_rota_health(client):
    response = client.get('/api/health')
    assert response.status_code == 200