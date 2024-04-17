import pytest
import requests
pytestmark = pytest.mark.api


@pytest.mark.duckduckgo
def test_duckduckgo_instant_answer_api():
    # Arrange
    url = 'https://api.duckduckgo.com/?q=python+programming&format=json&pretty=1'

    # Act
    response = requests.get(url)
    body = response.json()

    # Assert
    assert response.status_code == 200
    assert 'Python' in body['AbstractText']


@pytest.mark.pet_store
def test_available_pets_in_store():
    # Arrange
    url = "https://petstore3.swagger.io/api/v3/pet/findByStatus"
    
    # Act
    response = requests.get(url, params={"status": "available"},)
    body = response.json()

    # Assert
    assert response.status_code == 200
    for pet in body:
        assert pet['status'] == "available"
