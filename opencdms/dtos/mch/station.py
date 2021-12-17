from pydantic import BaseModel, constr
from typing import Optional
from decimal import Decimal


class Station(BaseModel):
    Station: Optional[str]
    StationName: Optional[str]
    StationName2: Optional[str]
    TimeZone: Optional[constr(max_length=4)]
    Longitud: Optional[Decimal]
    Latitud: Optional[Decimal]

    class Config:
        allow_population_by_field_name = True
        orm_mode = True
        fields = {
            "Station": "station_id",
            "StationName": "name",
            "StationName2": "secondary_name",
            "TimeZone": "timezone",
            "Longitud": "longitude",
            "Latitud": "latitude"
        }


class CreateStation(BaseModel):
    Station: str
    StationName: str

    class Config:
        fields = {
            "Station": "station_id",
            "StationName": "name",
            "StationName2": "secondary_name",
            "TimeZone": "timezone",
            "Longitud": "longitude",
            "Latitud": "latitude"
        }


class UpdateStation(BaseModel):
    StationName: Optional[str]

    class Config:
        fields = {
            "Station": "station_id",
            "StationName": "name",
            "StationName2": "secondary_name",
            "TimeZone": "timezone",
            "Longitud": "longitude",
            "Latitud": "latitude"
        }


class UniqueId(BaseModel):
    Station: str

    class Config:
        fields = {
            "Station": "station_id",
            "StationName": "name",
            "StationName2": "secondary_name",
            "TimeZone": "timezone",
            "Longitud": "longitude",
            "Latitud": "latitude"
        }
