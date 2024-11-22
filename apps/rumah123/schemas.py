from pydantic import BaseModel, Field


class FilterParams(BaseModel):
    base: str
    min_price: int
    min_land_area: int
    min_builtup_size: int
    max_land_area: int
    max_builtup_size: int
    max_page: int = 0


class PropertyDetails(BaseModel):
    title: str = Field(alias="Title")
    price: float = Field(alias="Price")
    location: str = Field(alias="Location")
    bedrooms: float = Field(alias="Bedrooms")
    bathrooms: float = Field(alias="Bathrooms")
    land_area: float = Field(alias="Land Area")
    building_area: float = Field(alias="Building Area")
    agent_name: str = Field(alias="Agent Name")
    url: str = Field(alias="URL")
    price_per_bedroom: float = Field(alias="Price per Bedroom")
    cost_per_bedroom: float = Field(alias="Cost per Bedroom")
    area_per_bedroom: float = Field(alias="Area per Bedroom")
