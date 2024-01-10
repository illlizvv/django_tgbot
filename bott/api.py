import requests
import json

BASE_URL = 'http://localhost:8000/api/v1'

def create_user(username, name, user_id):
    url = f"{BASE_URL}/bot-users"
    response = requests.get(url=url).text
    data = json.loads(response)
    user_exist = False
    for i in data:
        if i["user_id"] == str(user_id):
            user_exist = True
            break
    if user_exist == False:    
        requests.post(url=url, data={'username':username, "name":name, "user_id":user_id})
        return "Пользователь создан"
    else:
        return "Пользователь существует"
    
def create_feedback(user_id, body):
    url = f"{BASE_URL}/feedbacks"
    if body and user_id :
        post = requests.post(url=url, data = {
            "user_id":user_id,
            "body":body
        })
        return "Отправлено администратору."
    else:
        return "Сообщение не обработано"
    
def create_feedback1(user_id, body1):
    url = f"{BASE_URL}/feedbacks"
    if body1 and user_id :
        post = requests.post(url=url, data = {
            "user_id":user_id,
            "body1":body1
        })
        return "Отправлено администратору."
    else:
        return "Сообщение не обработано"
    
def create_feedback2(user_id, body2):
    url = f"{BASE_URL}/feedbacks"
    if body2 and user_id :
        post = requests.post(url=url, data = {
            "user_id":user_id,
            "body2":body2
        })
        return "Отправлено администратору."
    else:
        return "Сообщение не обработано"

def create_feedback3(user_id, body3):
    url = f"{BASE_URL}/feedbacks"
    if body3 and user_id :
        post = requests.post(url=url, data = {
            "user_id":user_id,
            "body3":body3
        })
        return "Отправлено администратору."
    else:
        return "Сообщение не обработано"

def create_feedback4(user_id, body4):
    url = f"{BASE_URL}/feedbacks"
    if body4 and user_id :
        post = requests.post(url=url, data = {
            "user_id":user_id,
            "body4":body4
        })
        return "Отправлено администратору."
    else:
        return "Сообщение не обработано"

def create_feedback5(user_id, body5):
    url = f"{BASE_URL}/feedbacks"
    if body5 and user_id :
        post = requests.post(url=url, data = {
            "user_id":user_id,
            "body5":body5
        })
        return "Отправлено администратору."
    else:
        return "Сообщение не обработано"
    
def update_subscription_status(user_id, subscribed):
    url = f"{BASE_URL}/bot-users/{user_id}/update"
    response = requests.patch(url=url, json={'subscribed': subscribed})
    return response.text


    