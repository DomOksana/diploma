import requests # импортирую бибилиотеку для отправки HTTP-зпросов
import allure   # для генерации отчетов
import pytest   # импортирую фреймворк с маркерами для отличия тестов по типу

URL = "https://petstore.swagger.io/v2/"  # адрес API для тестирования

"""
Поиск по ID
указываю функцию, заголовок, идентификатор м маркеры для теста

проверяю что ответ 200, или 400, или 404
если 200, то в ответе есть id и name, иначе "There is no pet ID" и "There is no pet name"
"""
@allure.feature("GET")
@allure.title("Поиск по ID")
@allure.id("1")
@pytest.mark.api_testing
@pytest.mark.new_features

def test_get_pet_id():
    pet_id = 111
    response = requests.get(
        url=f"{URL}pet/{pet_id}",
        headers={"accept": "application/json"})
    assert response.status_code in [200, 400, 404], f"error: {response.status_code}"

    if response.status_code == 200:
        pet_data = response.json()
        assert "id" in pet_data, "There is no pet ID"
        assert "name" in pet_data, "There is no pet name"
    elif response.status_code == 400:
        print("Invalid ID supplied")
    else:
        print("\nPet not found")
    print("\nPet was found")


"""
Поиск по статусу
проверяю что стсатусы могут быть: available, pending, sold
"""
@allure.feature("GET")
@allure.title("Поиск по статусу")
@allure.id("2")
@pytest.mark.api_testing
@pytest.mark.new_features

def test_pet_find_by_status():
    get_response = requests.get(
        url=f"{URL}pet/findByStatus",
        params={"status": "available"},
        headers={"accept": "application/json"})
    assert get_response.status_code == 200, f"error: запрос не выполнен"

    get_response = requests.get(
        url=f"{URL}pet/findByStatus",
        params={"status": "pending"},
        headers={"accept": "application/json"})
    assert get_response.status_code == 200, f"error: запрос не выполнен"

    get_response = requests.get(
        url=f"{URL}pet/findByStatus",
        params={"status": "sold"},
        headers={"accept": "application/json"})
    assert get_response.status_code == 200, f"error: запрос не выполнен"

    print()
    jsn = get_response.json()
    print(jsn)



