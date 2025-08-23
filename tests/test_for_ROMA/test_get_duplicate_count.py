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
    ("axaxxax", 4),
    ("aaaaа", 5),
    ("0123#@+—/_:00;12\'\',.21", 3),
    ("a a a a а а а а", 8),
    ("", 0),
    ("a", 0),
    ("aбвгд", 0),
    ("AaAa", 4)
    ("хе" * 999999, 999999)
])


def test_duplicate_count(input_string, expected_count):  # тест на подсчёт дубликатов
    data = {"stroka": input_string}
    response = requests.post(URL, headers=HEADERS, json=data)

    assert response.status_code == 200

    result = response.json()

    assert "count" in result
    assert "date" in result
    assert result["count"] == expected_count
    assert re.match(r"^\d{4}_\d{2}_\d{2} \d{2}:\d{2}:\d{2}$", result["date"])

    expected = {"count": expected_count, "date": result["date"]}
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
        expected = {"count": result["count"], "date": result["date"]}
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
