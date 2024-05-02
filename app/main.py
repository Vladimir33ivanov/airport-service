from fastapi import FastAPI, APIRouter
import httpx
from fastapi import APIRouter, HTTPException

app = FastAPI(openapi_url="/api/v1/airports/openapi.json", docs_url="/api/v1/airports/docs")

airports_router = APIRouter()

airports = [
    {
        'airports_id': 1,
        'name': 'Шереметьево',
        'description': 'Международный аэропорт в Москве.',
        'address': 'Аэропорт "Шереметьево", г. Химки, Московская обл., Россия',
        'country': 'Россия'
    },
    {
        'airports_id': 2,
        'name': 'Дубайский международный аэропорт',
        'description': 'Крупнейший аэропорт в мире по пассажиропотоку.',
        'address': 'Дубай, ОАЭ',
        'country': 'ОАЭ'
    },
    {
        'airports_id': 3,
        'name': 'Лондонский Хитроу',
        'description': 'Один из крупнейших и самых загруженных аэропортов мира.',
        'address': 'Хилтон-роуд, Хайтроу, Лондон, Великобритания',
        'country': 'Великобритания'
    },
    {
        'airports_id': 4,
        'name': 'Пекинский аэропорт имени Капитана Фана Цзыкя',
        'description': 'Один из крупнейших аэропортов в мире.',
        'address': 'Пекин, Китай',
        'country': 'Китай'
    },
    {
        'airports_id': 5,
        'name': 'Делийский аэропорт',
        'description': 'Один из крупнейших и самых загруженных аэропортов Индии.',
        'address': 'Нью-Дели, Индия',
        'country': 'Индия'
    }
]


@airports_router.get("/")
async def read_airports():
    return airports


@airports_router.get("/{airports_id}")
async def read_airport(airports_id: int):
    for airport in airports:
        if airport['airports_id'] == airports_id:
            return airport
    return None


app.include_router(airports_router, prefix='/api/v1/airports', tags=['airports'])

if __name__ == '__main__':
    import uvicorn
    import os

    try:
        PORT = int(os.environ['PORT'])
    except KeyError as keyerr:
        PORT = 80
    uvicorn.run(app, host='0.0.0.0', port=PORT)
