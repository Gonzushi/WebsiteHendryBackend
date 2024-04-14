from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    description: str
    price: int
    brand_id: int | None


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass


class Product(ProductBase):
    id: int

    class Config:
        from_attributes = True


class BrandBase(BaseModel):
    name: str


class BrandRead(BrandBase):
    id: int


class BrandReads(BaseModel):
    total: int
    records: list[BrandRead]


class BrandCreate(BrandBase):
    pass


class BrandUpdate(BrandBase):
    pass


class Brand(BrandBase):
    id: int
    products: list[Product] = []

    class Config:
        from_attributes = True
