from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

users = {}


class User(BaseModel):
    name: str
    email: str
    password: str


@app.get('/users/')
def get_users():
    return users.values()


@app.get('/users/{user_id}')
def get_user(user_id: int):
    return users[user_id]


@app.post('/users/', status_code=201)
def add_user(user: User):
    user_id = len(users) + 1
    users[user_id] = user
    return user_id


@app.put('/users/{user_id}')
def update_user(user_id: int, user: User):
    users[user_id] = user
    return user


@app.delete('/users/{user_id}')
def delete_user(user_id: int):
    del users[user_id]
    return user_id
