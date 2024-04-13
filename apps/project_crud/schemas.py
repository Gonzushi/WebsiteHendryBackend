from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    description: str
    price: int
    brand_id: int


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int

    class Config:
        from_attributes = True


class BrandBase(BaseModel):
    name: str


class BrandCreate(BrandBase):
    pass


class Brand(BrandBase):
    id: int
    products: list[Product] = []

    class Config:
        from_attributes = True
