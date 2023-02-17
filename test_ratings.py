from json import dumps
import requests
from assertpy.assertpy import assert_that


def test_get_all_ratings():
    response = requests.get("http://127.0.0.1:8000/ratings", timeout=10)
    assert_that(response.status_code).is_equal_to(requests.codes.ok)
    
def test_get_a_rating():
    response = requests.get("http://127.0.0.1:8000/ratings", timeout=10).json()
    first_name = [rating['first_name'] for rating in response]
    assert_that(first_name).contains('Jose')
    
def test_create_a_rating():
    payload = dumps({
        "rating_id":1,
        "booking_id":1,
        "stars":5,
        "first_name":"Jose",
        "last_name":"Otero",
        "comments":"Hi it is a excelent service.",
        "created_at":"2023-02-16T18:31:41.991612"
        })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    response = requests.post("http://127.0.0.1:8000/ratings", data=payload, headers=headers, timeout=10)
    assert_that(response.status_code).is_equal_to(requests.codes.created)
