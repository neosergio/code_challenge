def test_home_page_with_fixture(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """
    response = test_client.get("/")
    assert response.status_code == 200


def test_calculate_with_valid_numbers(test_client):
    """
    GIVEN a Flask application
    WHEN the '/calculate' endpoint is requested (GET) with list of numbers
    THEN check that the response is valid and proper calculation
    """
    response = test_client.get("/calculate?numbers=1,8,6,2,5,4,8,3,7")
    assert response.status_code == 200
    assert response.json["max_area"] == 49


def test_calculate_with_invalid_numbers(test_client):
    """
    GIVEN a Flask application
    WHEN the '/calculate' endpoint is requested (GET) with a text
    THEN check that the response is valid and error message is shown
    """
    response = test_client.get("/calculate?numbers=text")
    assert response.status_code == 200
    assert response.json["error"] == "no numbers in list"


def test_calculate_with_no_parameters(test_client):
    """
    GIVEN a Flask application
    WHEN the '/calculate' endpoint is requested (GET) with no parameter
    THEN check that the response is valid and max_area is null / none
    """
    response = test_client.get("/calculate")
    assert response.status_code == 200
    assert response.json["max_area"] is None
