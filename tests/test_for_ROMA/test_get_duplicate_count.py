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
    assert response.status_code == 200, f"Ожидался статус код 200, получен {response.status_code}"
    return response

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
    ("xexe", 2),
    ("axaxxax", 4),
    ("aaaaa", 5),
    ("0123#@+—/_:0'0;12,.21", 3),
    (" хехехе хехехе  ", 6),
    ("хх", 2),
    ("хе", 0),
    ("", 0),
    ("🙂🙂🙂", 3),
    ("🙂🙃🙂", 2),
    ("абвгдежзийклмнопрстуфхцчшщъыьэюя0123456789", 0),
    ("abcdefghijklmnopqrstuvwxyz0123456789", 0),
    ("ё", 0),
    ("AaAaAaAa", 8),
    ("хе" * 106, 106)
])


def test_check_api_duplicate_count(input_string, expected_count):
    response = get_api_response(input_string)

    result = response.json()
    check_input_data_field(result, input_string)
    check_count_field(result, expected_count)
    check_date_field(result)


def test_empty_body(): # тест с пустым боди: должна быть ошибка валидации
    response = requests.post(URL, headers=HEADERS, json={})
    assert response.status_code == 422, f"Ожидался статус 422, получен {response.status_code}"

    result = response.json()
    assert "detail" in result, "Отсутствует ключ 'detail' в ответе"
    assert isinstance(result["detail"], list), f"'detail' должен быть списком, получено {type(result['detail'])}"

    error = result["detail"][0]
    assert "loc" in error and error["loc"] == ["body", "stroka"], f"Неверное значение loc: {error.get('loc')}"
    assert "msg" in error and "required" in error["msg"].lower(), f"Ожидалось слово 'required', получено: {error.get('msg')}"
    assert "type" in error and "missing" in error["type"], f"Ожидался type='missing', получено: {error.get('type')}"


def test_wrong_field_name(): # тест на "мусорные" данные: должна быть 422
    data = {"string": "test"} # тут должно быть "stroka"
    response = requests.post(URL, headers=HEADERS, json=data)
    assert response.status_code == 422, f"Ожидался статус 422, получен {response.status_code}"

    result = response.json()
    assert "detail" in result, "Отсутствует ключ 'detail' в ответе"
    assert isinstance(result["detail"], list), f"'detail' должен быть списком, получено {type(result['detail'])}"

    error = result["detail"][0]
    assert "loc" in error and error["loc"] == ["body", "stroka"], f"Неверное значение loc: {error.get('loc')}"
    assert "msg" in error and "required" in error["msg"].lower(), f"Ожидалось слово 'required', получено: {error.get('msg')}"
    assert "type" in error and "missing" in error["type"], f"Ожидался type='missing', получено: {error.get('type')}"



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

    response = requests.post(URL, headers=headers if headers else None, json=data)

    result = response.json()

    if is_bug and response.status_code != expected_status:
        pytest.fail(f"Известный баг: ожидался {expected_status}, получен {response.status_code}")
    assert response.status_code == expected_status, f"Ожидался статус {expected_status}, получен {response.status_code}"

    if expected_status == 200:
        assert "count" in result
    else:
        assert "detail" in result
        error_text = result["detail"].lower()
        assert "not authenticated" in error_text or "токен" in error_text, f"Неожиданное сообщение: {result['detail']}"
