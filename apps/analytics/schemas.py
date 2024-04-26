from pydantic import BaseModel


class VisitorBase(BaseModel):
    session_id: str
    ip_address: str
    country_code: str
    country_name: str
    region_name: str
    city_name: str
    latitude: float
    longitude: float
    zip_code: int
    time_zone: str
    asn: str
    asn_name: str
    is_proxy: str


class VisitorCreate(BaseModel):
    ip_address: str


class VisitorRead(VisitorBase):
    pass


class EventBase(BaseModel):
    session_id: str
    ip_address: str
    type: str
    description: str


class EventCreate(EventBase):
    session_id: str
