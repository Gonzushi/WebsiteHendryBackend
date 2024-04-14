from sqlalchemy.orm import Session

from apps.project_crud import models, schemas


def create_brand(db: Session, brand: schemas.BrandCreate):
    db_brand = models.Brand(**brand.model_dump())
    db.add(db_brand)
    db.commit()
    db.refresh(db_brand)
    return db_brand


def update_brand(db: Session, brand_id: int, brand: schemas.BrandUpdate):
    db_brand = db.query(models.Brand).get(brand_id)
    for key, value in brand.model_dump().items():
        setattr(db_brand, key, value)
    db.add(db_brand)
    db.commit()
    db.refresh(db_brand)
    return db_brand


def delete_brand(db: Session, brand_id: int):
    db_brand = db.get(models.Brand, brand_id)
    db.delete(db_brand)
    db.commit()


def get_brand(db: Session, brand_id: int):
    return db.get(models.Brand, brand_id)


def get_brands(db: Session, skip: int = 0, limit: int = 100) -> schemas.BrandReads:
    total: int = db.query(models.Brand).count()
    records = (
        db.query(models.Brand).order_by(models.Brand.id).offset(skip).limit(limit).all()
    )
    output = {"total": total, "records": records}
    return output


def get_brand_by_name(db: Session, brand_name: str):
    return db.query(models.Brand).filter(models.Brand.name == brand_name).first()


def create_product(db: Session, product: schemas.Product):
    db_product = models.Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def update_product(db: Session, product_id: int, product: schemas.ProductUpdate):
    db_product = db.query(models.Product).get(product_id)
    for key, value in product.model_dump().items():
        setattr(db_product, key, value)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def delete_product(db: Session, product_id: int):
    db_product = db.get(models.Product, product_id)
    db.delete(db_product)
    db.commit()


def get_product(db: Session, product_id: int):
    return db.get(models.Product, product_id)


def get_products(db: Session, skip: int = 0, limit: int = 100):
    return (
        db.query(models.Product)
        .order_by(models.Product.id)
        .offset(skip)
        .limit(limit)
        .all()
    )
