import pytest

from my_app import create_app


@pytest.fixture(scope="module")
def test_client():
    flask_app = create_app("settings.py")

    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            yield testing_client
