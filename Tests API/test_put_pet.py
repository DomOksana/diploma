import requests # импортирую бибилиотеку для отправки HTTP-зпросов
import allure   # для генерации отчетов
import pytest   # импортирую фреймворк с маркерами для отличия тестов по типу

URL = "https://petstore.swagger.io/v2/"  # адрес API для тестирования

"""
Обновление питомца и запрос инфо о нем
указываю функцию, заголовок, идентификатор м маркеры для теста

проверяю что ответ 200

"""
@allure.feature("PUT")
@allure.title("Обновление питомца")
@allure.id("1")
@pytest.mark.api_testing
@pytest.mark.new_features

def test_update_pet():
    data_pet = {
        "id": 222,
        "category": {
            "id": 2,
            "name": "kitten2"
        },
        "name": "Kicu",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 1,
                "name": "string"
            }
        ],
        "status": "available"}

    post_response = requests.post(
        url=f"{URL}pet",
        headers={"accept": "application/json",
                 "Content-Type": "application/json"},
        json=data_pet)
    assert post_response.status_code == 200, f"error: запрос не выполнен"

    pet_id = post_response.json()["id"]
    update_pet = {
        "id": 222,
        "category": {
            "id": 1,
            "name": "kitten2"
        },
        "name": "Kicu_22",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 1,
                "name": "string"
            }
        ],
        "status": "available"}

    put_response = requests.put(
        url=f"{URL}pet",
        headers={"accept": "application/json",
                 "Content-Type": "application/json"},
        json=update_pet)
    assert put_response.status_code == 200, f"error: {put_response.status_code}"

    get_response = requests.get(
        url=f"{URL}pet/{pet_id}",
        headers={"accept": "application/json"})
    assert get_response.status_code == 200, f"error: {get_response.status_code}"
    #print(get_response.json())

"""
Обновление части информации
указываю функцию, заголовок, идентификатор м маркеры для теста

проверяю что ответ 200
"""
    @allure.feature("PUT")
    @allure.title("Обновление параметра")
    @allure.id("2")
    @pytest.mark.api_testing
    @pytest.mark.new_features

def test_update_pet_param():
    post_response = requests.post(
        url=f"{URL}pet/44",
        params={"petid": 444,
                "name": "Kicu_4",
                "status": "available"},
        headers={"accept": "application/json"}
    )
    assert post_response.status_code == 200, f"error: запрос не выполнен"