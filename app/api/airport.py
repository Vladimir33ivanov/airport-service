from typing import List
from fastapi import APIRouter, HTTPException
from app.api.models import AirportOut, AirportIn, AirportUpdate
from app.api import db_manager
from app.api.service import is_label_present

airport = APIRouter()

@airport.post('/', response_model=AirportIn, status_code=201)
async def create_airport(payload: AirportIn):
    for label_id in payload.labels_id:
        if not is_label_present(label_id):
            raise HTTPException(status_code=404, detail=f"Label with given id:{label_id} not found")

    airport_id = await db_manager.add_airport(payload)
    response = {
        'id': airport_id,
        **payload.dict()
    }

    return response

@airport.get('/', response_model=List[AirportOut])
async def get_airports():
    return await db_manager.get_all_airports()

@airport.get('/{id}/', response_model=AirportOut)
async def get_airport(id: int):
    airport = await db_manager.get_airport(id)
    if not airport:
        raise HTTPException(status_code=404, detail="airport not found")
    return airport

@airport.put('/{id}/', response_model=AirportOut)
async def update_airport(id: int, payload: AirportUpdate):
    airport = await db_manager.get_airport(id)
    if not airport:
        raise HTTPException(status_code=404, detail="Label not found")

    update_data = payload.dict(exclude_unset=True)

    if 'labels_id' in update_data:
        for label_id in payload.labels_id:
            if not is_label_present(label_id):
                raise HTTPException(status_code=404, detail=f"Label with given id:{label_id} not found")

    airport_in_db = AirportIn(**airport)

    updated_airport = airport_in_db.copy(update=update_data)

    return await db_manager.update_airport(id, updated_airport)

@airport.delete('/{id}/', response_model=None)
async def delete_airport(id: int):
    airport = await db_manager.get_airport(id)
    if not airport:
        raise HTTPException(status_code=404, detail="airport not found")
    return await db_manager.delete_airport(id)