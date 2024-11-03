import pandas as pd
from sqlalchemy.orm import Session

from apps.project_map import models, schemas


def create_location(db: Session, location: schemas.LocationCreate):
    db_location = models.Location(**location.model_dump())
    db.add(db_location)
    db.commit()
    db.refresh(db_location)
    return db_location


def update_location(db: Session, location_id: int, location: schemas.LocationUpdate):
    db_location = db.query(models.Location).get(location_id)
    if not db_location:
        return None  # Optionally raise an exception if the location is not found
    for key, value in location.model_dump().items():
        setattr(db_location, key, value)
    db.add(db_location)
    db.commit()
    db.refresh(db_location)
    return db_location


def delete_location(db: Session, location_id: int):
    db_location = db.get(models.Location, location_id)
    if db_location:
        db.delete(db_location)
        db.commit()


def get_location(db: Session, location_id: int):
    return db.get(models.Location, location_id)


def get_locations(
    db: Session, skip: int = 0, limit: int = 100
) -> schemas.LocationReads:
    total: int = db.query(models.Location).count()
    records = (
        db.query(models.Location)
        .order_by(models.Location.id.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )
    output = {"total": total, "records": records}
    return output


def get_location_by_phone(db: Session, phone_number: str):
    return (
        db.query(models.Location)
        .filter(models.Location.phone_number == phone_number)
        .first()
    )


