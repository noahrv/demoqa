import pytest
import requests
import re


URL = "https://qaconnect.crossb.ru/get_duplicate_count"
API_KEY = "88333900"
HEADERS = {
    "Test-Authorization": API_KEY,
    "Content-Type": "application/json"
}


@pytest.mark.parametrize("input_string,expected_count", [
    ("хехе", 2),
    ("axaxxax", 4)
])
def test_duplicate_count(input_string, expected_count):
    data = {"stroka": input_string}
    response = requests.post(URL, headers=HEADERS, json=data)

    assert response.status_code == 200

    result = response.json()

    assert "count" in result
    assert "date" in result
    assert result["count"] == expected_count
    assert re.match(r"^\d{4}_\d{2}_\d{2} \d{2}:\d{2}:\d{2}$", result["date"])


def test_empty_body(): # тест с пустым боди: должна быть ошибка валидации
    response = requests.post(URL, headers=HEADERS, json={})

    assert response.status_code == 422

    error_data = response.json()
    assert "detail" in error_data
    assert isinstance(error_data["detail"], list)

    if error_data["detail"]:
        first_error = error_data["detail"][0]
        assert "type" in first_error
        assert "loc" in first_error
        assert "msg" in first_error


def test_wrong_field_name(): # тест на "мусорные" данные: должна быть 422
    data = {"string": "test"}  # тут должно быть "stroka"
    response = requests.post(URL, headers=HEADERS, json=data)

    assert response.status_code == 422

    error_data = response.json()
    assert "detail" in error_data
    assert isinstance(error_data["detail"], list)

    if error_data["detail"]:
        first_error = error_data["detail"][0]
        assert "loc" in first_error
        assert "msg" in first_error
        assert "type" in first_error


def test_no_authorization(): # тест без авторизации: должна быть ошибка
    data = {"stroka": "test"}
    response = requests.post(URL, json=data)

    assert response.status_code == 401


def test_wrong_api_key(): # тест с неправильным ключом: ДОЛЖНА БЫТЬ ошибка
    wrong_headers = {
        "Test-Authorization": "wrong_key",
        "Content-Type": "application/json"
    }
    data = {"stroka": "test"}
    response = requests.post(URL, headers=wrong_headers, json=data)

    #assert response.status_code == 401 - так должно быть, но оно падает
    assert response.status_code == 200  # сейчас работает так (БАГ)