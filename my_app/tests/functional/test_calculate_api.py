def test_home_page_with_fixture(test_client):
    response = test_client.get("/")
    assert response.status_code == 200


def test_calculate_with_valid_numbers(test_client):
    response = test_client.get("/calculate?numbers=1,8,6,2,5,4,8,3,7")
    assert response.status_code == 200
    assert response.json["max_area"] == 49


def test_calculate_with_invalid_numbers(test_client):
    response = test_client.get("/calculate?numbers=text")
    assert response.status_code == 200
    assert response.json["error"] == "no numbers in list"


def test_calculate_with_no_parameters(test_client):
    response = test_client.get("/calculate")
    assert response.status_code == 200
    assert response.json["max_area"] is None
