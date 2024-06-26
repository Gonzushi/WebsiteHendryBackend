from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session

from apps.project_crud import crud, schemas
from apps.sql.database import get_db

router = APIRouter(
    prefix="/project_crud",
    tags=["Project CRUD"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


@router.post("/brand/", response_model=schemas.Brand)
def create_brand(brand: schemas.BrandCreate, db: Session = Depends(get_db)):
    db_brand = crud.get_brand_by_name(db=db, brand_name=brand.name)
    if db_brand:
        raise HTTPException(status_code=400, detail="Brand already registered")
    return crud.create_brand(db=db, brand=brand)


@router.put("/brand/{brand_id}", response_model=schemas.Brand)
def update_brand(
    brand_id: int, brand: schemas.BrandUpdate, db: Session = Depends(get_db)
):
    db_brand = crud.get_brand(db, brand_id)
    if db_brand is None:
        raise HTTPException(status_code=400, detail="Brand not found")
    db_brand = crud.get_brand_by_name(db=db, brand_name=brand.name)
    if db_brand:
        raise HTTPException(status_code=400, detail="Brand already registered")
    return crud.update_brand(db=db, brand_id=brand_id, brand=brand)


@router.delete("/brand/{brand_id}", status_code=204)
def delete_brand(brand_id: int, db: Session = Depends(get_db)):
    db_brand = crud.get_brand(db, brand_id)
    if db_brand is None:
        raise HTTPException(status_code=400, detail="Brand not found")
    crud.delete_brand(db=db, brand_id=brand_id)


@router.get("/brand/{brand_id}", response_model=schemas.Brand)
def read_brand(brand_id: int, db: Session = Depends(get_db)):
    db_brand = crud.get_brand(db, brand_id=brand_id)
    if db_brand is None:
        raise HTTPException(status_code=404, detail="Brand not found")
    return db_brand


@router.get("/brand/", response_model=schemas.BrandReads)
def read_brands(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    brands = crud.get_brands(db, skip=skip, limit=limit)
    return brands


@router.post("/product/", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    db_brand = crud.get_brand(db, brand_id=product.brand_id)
    if db_brand is None:
        raise HTTPException(status_code=404, detail="Brand ID not found")
    return crud.create_product(db=db, product=product)


@router.put("/product/{product_id}", response_model=schemas.Product)
def update_product(
    product_id: int, product: schemas.ProductUpdate, db: Session = Depends(get_db)
):
    db_product = crud.get_product(db, product_id)
    db_brand = crud.get_brand(db, product.brand_id)
    if db_brand is None:
        raise HTTPException(status_code=404, detail="Brand ID not found")
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return crud.update_product(db=db, product_id=product_id, product=product)


@router.delete("/product/{product_id}", status_code=204)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    db_product = crud.get_product(db, product_id)
    if db_product is None:
        raise HTTPException(status_code=400, detail="Product not found")
    crud.delete_product(db=db, product_id=product_id)


@router.get("/product/{product_id}", response_model=schemas.Product)
def read_product(product_id: int, db: Session = Depends(get_db)):
    db_product = crud.get_product(db, product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product


@router.get("/product/", response_model=schemas.ProductReads)
def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = crud.get_products(db, skip=skip, limit=limit)
    return products


@router.get("/", response_model=schemas.AllData)
def read_all_data(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    data = crud.get_all_data(db, skip=skip, limit=limit)
    return data
