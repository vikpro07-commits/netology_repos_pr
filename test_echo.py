import requests

# Базовый URL вынесен в константу для удобства
BASE_URL = "https://postman-echo.com"

def test_get_request_with_params():
    """Тест GET-запроса с передачей query-параметров."""
    response = requests.get(f"{BASE_URL}/get", params={"test_param": "123"})
    
    # Проверяем статус-код
    assert response.status_code == 200, f"Ожидался 200, получено {response.status_code}"
    
    # Проверяем, что Postman Echo вернул переданный параметр
    response_data = response.json()
    assert response_data["args"]["test_param"] == "123", "Параметр 'test_param' не совпадает"

def test_post_request_with_json():
    """Тест POST-запроса с отправкой JSON-тела."""
    payload = {"name": "QA_Student", "role": "Tester"}
    response = requests.post(f"{BASE_URL}/post", json=payload)
    
    assert response.status_code == 200
    # Echo возвращает отправленный JSON в ключе 'data'
    assert response.json()["data"]["name"] == "QA_Student"

def test_put_request_with_text():
    """Тест PUT-запроса для обновления данных (простой текст)."""
    response = requests.put(f"{BASE_URL}/put", data="Plain text update")
    
    assert response.status_code == 200
    assert response.json()["data"] == "Plain text update"

def test_delete_request():
    """Тест DELETE-запроса."""
    response = requests.delete(f"{BASE_URL}/delete", params={"id": 1})
    
    assert response.status_code == 200
    # Параметры запроса возвращаются как строки
    assert response.json()["args"]["id"] == "1"

def test_custom_headers():
    """Тест отправки кастомных заголовков (Headers)."""
    headers = {"My-Custom-Header": "SecretValue"}
    response = requests.get(f"{BASE_URL}/get", headers=headers)
    
    assert response.status_code == 200
    # Postman Echo переводит все заголовки в нижний регистр
    assert response.json()["headers"]["my-custom-header"] == "SecretValue"