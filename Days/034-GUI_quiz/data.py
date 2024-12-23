import requests

API_ENDPOINT = "https://opentdb.com/api.php?amount=10&type=boolean"


def get_data():
    response = requests.get(API_ENDPOINT)
    response.raise_for_status()
    data = response.json()
    return data["results"]


question_data: list = get_data()
