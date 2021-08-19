# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 13:07:51 2020
@author: win10
"""
# pip install fastapi uvicorn

# 1. Library imports
import uvicorn  # ASGI
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3. Index route, opens automatically on http://127.0.0.1:8000


@app.get('/')
def index():
    return {'message': 'Hello, World'}


@app.get('/dawnNews')
def get_dawn_news():
    fake_news = [
        'Pakistan will negotiate with Afghanistan',
        'Indian threatned pakistan with dire consequences',
        'Pakistan launched it''s second missile'
    ]
    real_news = [
        'Petrol prices will reach to new level',
        'Different degree of police officers has been deployed',
        'army will confirm targetting indian basis'
    ]
    total_news_count = len(fake_news)+len(real_news)
    return {'TotalNews': str(total_news_count), "fake_news": fake_news, "real_news": real_news}


@app.get('/wait')
async def wait_for_me():
    time.sleep(4)
    return ('you waited and the reward is :)')


@app.get('/users', tags=['User'])
async def get_users() -> dict:
    return {"users": users}

@app.get('/users/{id}',tags=['User'])
async def get_single_user(id:int)->dict:
    try:
        single_user = users[id]
        return {"data":single_user,"flag":True}
    except Exception as e:
        return {"error":str(e),"flag":False}

@app.post('/users',tags=['User'])
async def post_single_user(user:dict)->dict:
    try:
        users.append(user)
        return {"data":user,"flag":True}
    except Exception as e:
        return {"error":str(e),"flag":False}

@app.put('/users/{id}',tags=['User'])
async def update_single_user(id:int,user:dict)->dict:
    try:
        users[id]['userName'] = user['userName']
        users[id]['userFullName'] = user['userFullName']
        users[id]['userEmail'] = user['userEmail']
        return {"data":users[id],"flag":True}
    except Exception as e:
        return {"error":str(e),"flag":False}
@app.delete('/users/{id}',tags=['User'])
async def delete_single_user(id:int)->dict:
    try:
        users.remove(id)
        return {"data":id,"flag":True}
    except Exception as e:
        return {"error":str(e),"flag":False}

users = [{
    "id": 0,
    "userName": "j33mk",
    "userFullName": "jamal hussain",
    "userEmail": "xyz@gmail.com"
}, {
    "id": 1,
    "userName": "ahsan",
    "userFullName": "Ahsan Abbas",
    "userEmail": "ahsan@xyz.com"
}
]

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
# if __name__ == '__main__':
#     uvicorn.run(app, host='127.0.0.1', port=8000,reload=True)
# uvicorn main:app --reload
