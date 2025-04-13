import pytest
from utils.api import GoogleMapsAPI

@pytest.fixture
def created_place():
    response = GoogleMapsAPI.create_new_place()
    place_id = response.json().get('place_id')
    return place_id