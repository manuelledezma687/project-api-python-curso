import requests
from assertpy.assertpy import assert_that


def test_get_all_ratings():
    response = requests.get("http://127.0.0.1:8000/ratings", timeout=10)
    assert_that(response.status_code).is_equal_to(requests.codes.ok)
    
def test_get_a_rating():
    response = requests.get("http://127.0.0.1:8000/ratings", timeout=10).json()
    first_name = [rating['first_name'] for rating in response]
    assert_that(first_name).contains('Jose')