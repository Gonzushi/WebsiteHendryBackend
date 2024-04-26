from pydantic import BaseModel


class Visitor(BaseModel):
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


class Event(BaseModel):
    session_id: str
    ip_address: str
    type: str
    description: str


class PageViewSummary(BaseModel):
    path: str
    total: int
