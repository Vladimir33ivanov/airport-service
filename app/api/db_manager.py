from app.api.models import AirportIn

from app.api.db import airports, database


async def add_airport(payload: AirportIn):
    query = airports.insert().values(**payload.dict())
    return await database.execute(query=query)


async def airports():
    query = airports.select()
    return await database.fetch_all(query=query)


async def get_airport(id):
    query = airports.select(airports.c.id == id)
    return await database.fetch_one(query=query)


async def delete_airport(id: int):
    query = airports.delete().where(airports.c.id == id)
    return await database.execute(query=query)


async def update_airport(id: int, payload: AirportIn
):
    query = (
        airports
        .update()
        .where(airports.c.id == id)
        .values(**payload.dict())
    )
    return await database.execute(query=query)
