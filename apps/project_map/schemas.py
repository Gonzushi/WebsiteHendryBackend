from pydantic import BaseModel


class LocationBase(BaseModel):
    latitude: float
    longitude: float
    phone_number: str | None
    area: int | None
    type: str | None
    price: float | None
    comment: str | None


class LocationCreate(LocationBase):
    pass


class LocationRead(LocationBase):
    id: int


class LocationUpdate(LocationBase):
    pass


class LocationReads(BaseModel):
    total: int
    records: list[LocationRead]


class Location(LocationBase):
    id: int

    class Config:
        from_attributes = True
