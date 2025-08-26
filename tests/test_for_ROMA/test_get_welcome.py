import pytest
import requests


BASE_URL = "https://qaconnect.crossb.ru"

def test_get_welcome():
    url = f"{BASE_URL}/get_welcome"
    response = requests.get(url)

    assert response.status_code == 200, f"Ожидался статус 200, но получен {response.status_code}"

    data = response.json()
    assert isinstance(data, str), f"Ожидался тип str, но получен {type(data).__name__}"
    assert data.strip() != "", f"Ответ пустой: '{data}'"

    valid_responses = [
        "Добро пожаловать!",
        "Привет! Мы ждали именно тебя!",
        "Ваше путешествие начинается здесь!"
    ]

    assert data in valid_responses, f"Ответ '{data}' не входит в список допустимых: {valid_responses}"
