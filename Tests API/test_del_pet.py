import requests # импортирую бибилиотеку для отправки HTTP-зпросов
import allure   # для генерации отчетов
import pytest   # импортирую фреймворк с маркерами для отличия тестов по типу

URL = "https://petstore.swagger.io/v2/"  # адрес API для тестирования

"""
Удаление по ID
указываю функцию, заголовок, идентификатор м маркеры для теста

проверяю что ответ 200, или 404

"""

@allure.feature("DELETE")
@allure.title("Удаление по ID")
@allure.id("1")
@pytest.mark.api_testing
@pytest.mark.new_features
def test_delete_pet():
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
    assert post_response.status_code == 200, f"error: {post_response.status_code}"
    pet_id = post_response.json()["id"]

    delete_response = requests.delete(
        url=f"{URL}pet/{pet_id}",
        headers={"accept": "application/json"})
    assert delete_response.status_code == 200, f"error: {delete_response.status_code}"

    get_response = requests.get(
        url=f"{URL}pet/{pet_id}",
        headers={"accept": "application/json"})
    assert get_response.status_code == 404, f"pet {pet_id} still exists"

    delete_response = requests.delete(
        url=f"{URL}pet/{pet_id}",
        headers={"accept": "application/json"})
    assert delete_response.status_code == 404, f"pet {pet_id} still exists"