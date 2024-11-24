from fastapi import FastAPI, Path
from fastapi.responses import JSONResponse
from typing import Annotated

app = FastAPI()


@app.get('/')
async def get_main_page() -> JSONResponse:
    return JSONResponse(content='Главная страница',
                        headers={'Content-Type': 'charset=utf-8'})


@app.get('/user/admin')
async def get_admin_page() -> JSONResponse:
    return JSONResponse(content='Вы вошли как администратор',
                        headers={'Content-Type': 'charset=utf-8'})


@app.get('/user/{user_id}')
async def get_user_id(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example='1')]) -> JSONResponse:
    return JSONResponse(content=f'Вы вошли как пользователь № {user_id}',
                        headers={'Content-Type': 'charset=utf-8'})


@app.get('/user/{username}/{age}')
async def get_user_info(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
                        age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='24')]) -> JSONResponse:
    if username is None and age is None:
        return JSONResponse(content='Не заданы параметры пользователя',
                            headers={'Content-Type': 'charset=utf-8'})
    if username is None:
        return JSONResponse(content='Не задан username пользователя',
                            headers={'Content-Type': 'charset=utf-8'})
    if age is None:
        return JSONResponse(content=f'Информация о пользователе. Имя: {username}, Возраст: не задан',
                            headers={'Content-Type': 'charset=utf-8'})
    else:
        return JSONResponse(content=f'Информация о пользователе. Имя: {username}, Возраст: {age}',
                            headers={'Content-Type': 'charset=utf-8'})
