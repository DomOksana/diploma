
import requests
import json
import pytest

# метод GET /pet/{petID}
def test_get_pet_by_id():
    # запрос по поиску питомца:  GET /pet
    response = requests.get("https://petstore.swagger.io/v2/pet/1")
    # проверка статуса ответа
    assert response.status_code == 200
    # проверка ID в ответе
    assert response.json()["id"] == 1

# метод POST /pet
def test_post_pet():
    # параметры запроса
    data = {
        "id": 1,
        "name": "my_muw",
        "photoUrls": ["нет_фото"],
        "tags": [{"name": "string"}],
        "status": "available"
    }

    # указываю headers
    headers = {
        "Content-Type": "application/json"
    }

    # запрос по созданию питомца:  POST /pet
    response = requests.post("https://petstore.swagger.io/v2/pet", json=data, headers=headers)

    # проверка статуса ответа
    assert response.status_code == 200

    # проверка имени созданного питомца
    assert response.json()["name"] == "my_muw"

# метод POST /pet/{pet_id}/uploadImage
# def test_upload_pet_image():
#     # параметры запроса
#     pet_id = 1
#     file_path = "C:\Users\admin\Desktop\Pet1.png"
#     file = open(file_path, 'rb')
#     headers = {
#         "Content-Type": "image/jpeg"
#     }
#
#     # запрос по добавлению фота питомца POST /pet/{pet_id}/uploadImage
#     response = requests.post(f"https://petstore.swagger.io/v2/pet/{pet_id}/uploadImage", files={"file": file}, headers=headers)
#
#     # проверка статуса ответа
#     assert response.status_code == 200
#
#     # проверка текста в  ответе
#     assert response.json()["code"] == 200

# метод PUT /pet
def test_update_pet():
    # параметры запроса
    pet_id = 1
    data = {
        "id": pet_id,
        "name": "my_muw2",
        "photoUrls": ["нет_фото"],
        "tags": [{"name": "string"}],
        "status": "available"
    }

    # указываю headers
    headers = {
        "Content-Type": "application/json"
    }

    # запрос по редактированию питомца:  PUT /pet
    response = requests.put(f"https://petstore.swagger.io/v2/pet/{pet_id}", json=data, headers=headers)

    # проверка статуса ответа
    assert response.status_code == 200

    # проверка текста в ответе
    assert response.json()["name"] == "my_muw2"
