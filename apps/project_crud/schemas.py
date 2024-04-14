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


class ProductRead(ProductBase):
    id: int


class ProductReads(BaseModel):
    total: int
    records: list[ProductRead]


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


class Data(BaseModel):
    product_name: str
    brand_name: str
    description: str
    price: int
    brand_id: int
    product_id: int


class AllData(BaseModel):
    total: int
    records: list[Data]
