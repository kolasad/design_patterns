"""
Kolejnosc importow:
1. Importy bibliotek Pythona
2. Zainstalowane moduly/paczki
3. Nasze moduly
"""

import os

import requests

from constants import (
    DISEASES_LIMIT_FOR_VISIT, REQUIRED_DAYS_FROM_LAST_VISIT, YESTERDAY_VISIT
)
from main import check_name


def should_visit_doctor(days_from_last_visit, diseases: list = None):
    """
    Gives recommendation on doctor visit
    :param days_from_last_visit: days_from_last_visit
    :param diseases: diseases
    :return: bool, if we should visit a doctor
    """
    number_of_diseases = (
        len(diseases) if diseases else 0
    )  # get number of diseases if exists

    if days_from_last_visit > YESTERDAY_VISIT and number_of_diseases > DISEASES_LIMIT_FOR_VISIT:
        return True
    elif days_from_last_visit > REQUIRED_DAYS_FROM_LAST_VISIT:
        return True
    return False


assert should_visit_doctor(3, diseases=["a", "b", "c", "d"]) is True
assert should_visit_doctor(9) is False
assert should_visit_doctor(12) is True

last_visited = True
if last_visited:
    print("True")

names = []
if names:
    print(names)  # will not print empty list


def get_text(site_url):
    return requests.get(site_url).text


check_name("Sam", "Is Sam in a car?")

print(os.environ)  # zmienne srodowiskowe
