from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from apps.project_map import crud, schemas
from apps.sql.database import get_db

router = APIRouter(
    prefix="/project_map",
    tags=["Project Map"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


@router.post("/location/", response_model=schemas.Location)
def create_location(location: schemas.LocationCreate, db: Session = Depends(get_db)):
    return crud.create_location(db=db, location=location)


@router.put("/location/{location_id}", response_model=schemas.Location)
def update_location(
    location_id: int, location: schemas.LocationUpdate, db: Session = Depends(get_db)
):
    db_location = crud.get_location(db, location_id)
    if db_location is None:
        raise HTTPException(status_code=404, detail="Location not found")
    return crud.update_location(db=db, location_id=location_id, location=location)


@router.delete("/location/{location_id}", status_code=204)
def delete_location(location_id: int, db: Session = Depends(get_db)):
    db_location = crud.get_location(db, location_id)
    if db_location is None:
        raise HTTPException(status_code=404, detail="Location not found")
    crud.delete_location(db=db, location_id=location_id)


@router.get("/location/{location_id}", response_model=schemas.Location)
def read_location(location_id: int, db: Session = Depends(get_db)):
    db_location = crud.get_location(db, location_id=location_id)
    if db_location is None:
        raise HTTPException(status_code=404, detail="Location not found")
    return db_location


@router.get("/location/", response_model=schemas.LocationReads)
def read_locations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    locations = crud.get_locations(db, skip=skip, limit=limit)
    return locations


@router.get("/location/phone/{phone_number}", response_model=schemas.Location)
def read_location_by_phone(phone_number: str, db: Session = Depends(get_db)):
    db_location = crud.get_location_by_phone(db, phone_number)
    if db_location is None:
        raise HTTPException(status_code=404, detail="Location not found")
    return db_location
