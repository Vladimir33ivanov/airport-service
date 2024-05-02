from pydantic import BaseModel
from typing import List, Optional


class AirportIn(BaseModel):
    name: str
    description: str
    address: str
    country: str
    plane_id: List[int]


class AirportOut(AirportIn):
    id: int


class ArtistUpdate(AirportIn):
    name: Optional[str] = None
    description: Optional[str] = None
    address: Optional[str] = None
    country: Optional[str] = None
    plane_id: Optional[List[int]] = None