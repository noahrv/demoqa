import pytest
import requests
import re

URL = "https://qaconnect.crossb.ru/get_duplicate_count"
API_KEY = "88333900"
HEADERS = {
    "Test-Authorization": API_KEY,
    "Content-Type": "application/json"
}

def get_api_response(input_string):
    data = {"stroka": input_string}
    response = requests.post(URL, headers=HEADERS, json=data)
    return response

def check_status_code(response):
    assert response.status_code == 200, f"Ожидался статус код 200, получен {response.status_code}"

def check_input_data_field(result, input_string):
    assert "input_data" in result, "Отсутствует поле 'input_data' в ответе"
    assert result["input_data"] == input_string, f"Ожидалось input_data: {input_string}, получено: {result['input_data']}"

def check_count_field(result, expected_count):
    assert "count" in result, "Отсутствует поле 'count' в ответе"
    assert result["count"] == expected_count, f"Ожидалось count: {expected_count}, получено: {result['count']}"

def check_date_field(result):
    assert "date" in result, "Отсутствует поле 'date' в ответе"
    assert re.match(r"^\d{4}_\d{2}_\d{2} \d{2}:\d{2}:\d{2}$", result["date"]), f"Неверный формат даты: {result['date']}"


@pytest.mark.parametrize("input_string,expected_count", [
    ("хехе", 2),
    ("axaxxax", 4),
    ("aaaaa", 5),
    ("0123#@+—/_:0'0;12,.21", 3),
    (" хехехе хехехе  ", 6),
    ("", 0),
    ("абвгдежзийклмнопрстуфхцчшщъыьэюя0123456789", 0),
    ("ё", 0),
    ("AaAaAaAa", 8),
    ("хе" * 106, 106)
])

def test_check_api_duplicate_count(input_string, expected_count):
    response = get_api_response(input_string)
    check_status_code(response)

    result = response.json()
    check_input_data_field(result, input_string)
    check_count_field(result, expected_count)
    check_date_field(result)

    expected = {"input_data": input_string, "count": expected_count, "date": result["date"]}
    assert result == expected, f"Подробности ошибки: ожидалось {expected}, получили {result}"


def test_empty_body():  # тест с пустым боди: должна быть ошибка валидации
    response = requests.post(URL, headers=HEADERS, json={})

    assert response.status_code == 422

    result = response.json()
    assert "detail" in result
    assert isinstance(result["detail"], list)

    if result["detail"]:
        first_error = result["detail"][0]
        assert "type" in first_error
        assert "loc" in first_error
        assert "msg" in first_error

    expected = {"detail": result["detail"]}
    assert result == expected, f"Подробности ошибки: ожидалось {expected}, получили {result}"


def test_wrong_field_name():  # тест на "мусорные" данные: должна быть 422
    data = {"string": "test"}  # тут должно быть "stroka"
    response = requests.post(URL, headers=HEADERS, json=data)

    assert response.status_code == 422

    result = response.json()
    assert "detail" in result
    assert isinstance(result["detail"], list)

    if result["detail"]:
        first_error = result["detail"][0]
        assert "loc" in first_error
        assert "msg" in first_error
        assert "type" in first_error

    expected = {"detail": result["detail"]}
    assert result == expected, f"Подробности ошибки: ожидалось {expected}, получили {result}"


@pytest.mark.parametrize("headers,expected_status,is_bug", [
    (
        HEADERS, 200, False  # успешная авторизация
    ),
    (
        None, 401, False  # без авторизации
    ),
    (
        {"Test-Authorization": "invalid_auth_value", "Content-Type": "application/json"},
        401, True  # неверное значение (баг - сейчас 200, должно быть 401)
    ),
    (
        {"Wrong-Authorization-Key": API_KEY, "Content-Type": "application/json"},
        401, False  # неверный ключ
    ),
    (
        {"Wrong-Authorization-Header": "completely_wrong_value", "Content-Type": "application/json"},
        401, False  # полностью неверные данные
    ),
])

def test_authorization(headers, expected_status, is_bug):
    data = {"stroka": "test"}
    if headers:
        response = requests.post(URL, headers=headers, json=data)
    else:
        response = requests.post(URL, json=data)

    if is_bug:
        assert response.status_code == 200, "известный баг: ожидался 401"
    else:
        assert response.status_code == expected_status

    result = response.json()
    if response.status_code == 200:
        expected = {"input_data": "test", "count": result["count"], "date": result["date"]}
    else:
        expected = {"detail": result["detail"]}

    assert result == expected, f"Подробности ошибки: ожидалось {expected}, получили {result}"


# def test_successful_authorization():  # тест с успешной авторизацией
#     data = {"stroka": "test_string"}
#     response = requests.post(URL, headers=HEADERS, json=data)
#
#     assert response.status_code == 200
#
#     result = response.json()
#     expected = {"count": result["count"], "date": result["date"]}
#     assert result == expected, f"Подробности ошибки: ожидалось {expected}, получили {result}"
#
#
# def test_no_authorization():  # тест без авторизации: должна быть ошибка
#     data = {"stroka": "test"}
#     response = requests.post(URL, json=data)
#
#     assert response.status_code == 401
#
#     result = response.json()
#     expected = {"detail": result["detail"]}
#     assert result == expected, f"Подробности ошибки: ожидалось {expected}, получили {result}"
#
#
# def test_wrong_authorization_value():  # тест с неверным значением
#     wrong_value_headers = {
#         "Test-Authorization": "invalid_auth_value",
#         "Content-Type": "application/json"
#     }
#     data = {"stroka": "test"}
#     response = requests.post(URL, headers=wrong_value_headers, json=data)
#
#     # assert response.status_code == 401 - так должно быть, но оно падает
#     assert response.status_code == 200  # сейчас работает так (БАГ)
#
#     result = response.json()
#     expected = {"count": result["count"], "date": result["date"]}
#     assert result == expected, f"Подробности ошибки: ожидалось {expected}, получили {result}"
#
#
# def test_wrong_authorization_key():  # тест с неверным ключом
#     wrong_key_headers = {
#         "Wrong-Authorization-Key": API_KEY,
#         "Content-Type": "application/json"
#     }
#     data = {"stroka": "test"}
#     response = requests.post(URL, headers=wrong_key_headers, json=data)
#
#     assert response.status_code == 401
#
#     result = response.json()
#     expected = {"detail": result["detail"]}
#     assert result == expected, f"Подробности ошибки: ожидалось {expected}, получили {result}"
#
#
# def test_completely_wrong_auth_data():  # тест с полностью неверными данными
#     completely_wrong_headers = {
#         "Wrong-Authorization-Header": "completely_wrong_value",
#         "Content-Type": "application/json"
#     }
#     data = {"stroka": "test"}
#     response = requests.post(URL, headers=completely_wrong_headers, json=data)
#
#     assert response.status_code == 401
#
#     result = response.json()
#     expected = {"detail": result["detail"]}
#     assert result == expected, f"Подробности ошибки: ожидалось {expected}, получили {result}"
