def test_get_elements(client):
    response = client.get(f"/people")
    assert response.status_code == 200
    data = response.json()

    assert len(data) == 82
    assert data[0]["name"] == "Luke Skywalker"
    assert data[0]["created"] == "2014-12-09T13:50:51.644000Z"
