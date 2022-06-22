from app.models.cars import Car

def test_get_all_cars_with_empty_db_returns_empty_list(client):
    response = client.get('/cars')
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []

def test_get_one_car_with_populated_db_returns_car_json(client, three_cars):
    response = client.get("/cars/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "driver": "Tanya",
        "team": "Ferrari",
        "mass_kg": 700
    }

def test_get_all_cars_with_populated_db_returns_car_json(client, three_cars):


def test_post_one_car_creates_car_in_db(client):
    response = client.post('/cars', json = {})

def test_get_one_car_with_empty_