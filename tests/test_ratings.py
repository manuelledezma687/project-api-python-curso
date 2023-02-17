from json import dumps
import allure
import requests
from assertpy.assertpy import assert_that
from config import Data
from utils.read_file import reader


@allure.title("Obtener todos los ratings")
@allure.link("www.ratings.com")
@allure.suite("Ratings")
def test_get_all_ratings():
    response = requests.get(Data.BASE_URI, timeout=10)
    assert_that(response.status_code).is_equal_to(requests.codes.ok)


@allure.title("Obtener un rating determinado")
@allure.link("www.ratings.com")
@allure.suite("Ratings")
def test_get_a_rating():
    response = requests.get(Data.BASE_URI, timeout=10).json()
    first_name = [rating['first_name'] for rating in response]
    assert_that(first_name).contains('Jose')


@allure.title("Crear un rating")
@allure.link("www.ratings.com")
@allure.suite("Ratings")
def test_create_a_rating():
    payload = dumps(reader('rating.json'))
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    response = requests.post(Data.BASE_URI, data=payload, headers=headers, timeout=10)
    assert_that(response.status_code).is_equal_to(requests.codes.created)
