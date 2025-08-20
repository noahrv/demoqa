import pytest
import requests


BASE_URL = "https://qaconnect.crossb.ru"


def test_get_welcome():
    url = f"{BASE_URL}/get_welcome"
    response = requests.get(url)

    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, str)
    assert data.strip() != ""

    key_phrases = [
        "Добро пожаловать!",
        "Привет! Мы ждали именно тебя",
        "Ваше путешествие начинается здесь!"
    ]

    assert any(phrase in data for phrase in key_phrases)
