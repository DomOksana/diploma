import requests # импортирую бибилиотеку для отправки HTTP-зпросов
import allure   # для генерации отчетов
import pytest   # импортирую фреймворк с маркерами для отличия тестов по типу

URL = "https://petstore.swagger.io/v2/"   # адрес API для тестирования

"""
Создание записи про питомца
указываю функцию, заголовок, идентификатор м маркеры для теста

проверяю что ответ 200 или  404

"""

@allure.feature("POST")
@allure.title("Создание записи про притомца")
@allure.id("1")
@pytest.mark.api_testing
@pytest.mark.new_features
@pytest.mark.smoke
def test_add_pet():
    data_pet = {
        "id": 333,
        "category": {
            "id": 1,
            "name": "kitten"
        },
        "name": "Kicune",
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

    response = requests.post(
        url=f"{URL}pet",
        headers={"accept": "application/json",
                 "Content-Type": "application/json"},
        json=data_pet)
    assert response.status_code == 200, f"Failed to create pet: {response.text}"

    pet_id = response.json()["id"]


    get_response = requests.get(
        url=f"{URL}pet/{pet_id}",
        headers={"accept": "application/json"})
    assert get_response.status_code == 200, f"Pet not found: {response.text}"

    get_response = requests.get(
        url=f"{URL}pet/777",
        headers={"accept": "application/json"})
    assert get_response.status_code == 404, f"Pet with ID 777 exists"



"""
Загружаю изображение
проверяю что ответ 200
если 200, то в ответе есть uploaded, иначе "File upload failed"
"""
@allure.feature("POST")
@allure.title("Загрузка изображения")
@allure.id("2")
@pytest.mark.api_testing
@pytest.mark.new_features

def test_upload_image():
    URL = "https://petstore.swagger.io/v2"
    pet_id = 333
    file_path = "Pet1.png"
    files = {"file": open(file_path, "rb")}

    response = requests.post(f"{URL}/pet/{pet_id}/uploadImage", files=files)
    assert response.status_code == 200, f"Failed to upload image: {response.text}"
    assert "uploaded" in response.text, "File upload failed"

    # print()
    # jsn = response.json()
    # print(jsn)