import os
import json
import requests

# ユーザー管理システムのサンプルコード

users = []

def add_user(name, age, email):
    user = {}
    user['name'] = name
    user['age'] = age
    user['email'] = email
    user['id'] = len(users) + 1
    users.append(user)
    return user

def get_user(id):
    for i in range(len(users)):
        if users[i]['id'] == id:
            return users[i]
    return None

def delete_user(id):
    for i in range(len(users)):
        if users[i]['id'] == id:
            users.pop(i)
            return True
    return False

def update_user(id, name=None, age=None, email=None):
    for i in range(len(users)):
        if users[i]['id'] == id:
            if name != None:
                users[i]['name'] = name
            if age != None:
                users[i]['age'] = age
            if email != None:
                users[i]['email'] = email
            return users[i]
    return None

def get_all_users():
    result = []
    for i in range(len(users)):
        result.append(users[i])
    return result

def save_users_to_file(filename):
    with open(filename, 'w') as f:
        json.dump(users, f)

def load_users_from_file(filename):
    global users
    with open(filename, 'r') as f:
        users = json.load(f)

def search_users(query):
    result = []
    for i in range(len(users)):
        if query in users[i]['name'] or query in users[i]['email']:
            result.append(users[i])
    return result

def fetch_user_from_api(user_id):
    url = "http://api.example.com/users/" + str(user_id)
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return data

def validate_user(name, age, email):
    if name == None or name == "":
        return False
    if age == None:
        return False
    if age < 0 or age > 150:
        return False
    if email == None or email == "":
        return False
    if "@" not in email:
        return False
    return True

def print_user(user):
    print("ID: " + str(user['id']))
    print("名前: " + user['name'])
    print("年齢: " + str(user['age']))
    print("メール: " + user['email'])

if __name__ == "__main__":
    add_user("田中太郎", 30, "tanaka@example.com")
    add_user("山田花子", 25, "yamada@example.com")
    add_user("鈴木一郎", 40, "suzuki@example.com")

    print("全ユーザー:")
    for user in get_all_users():
        print_user(user)
        print("---")

    save_users_to_file("users.json")
    print("保存完了")
