import uuid

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from apps.analytics import crud, models, schemas
from apps.sql.database import get_db

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


@router.post("/event")
def create_event(
    event: schemas.Event,
    db: Session = Depends(get_db),
):
    visitor: models.Visitor = crud.get_visitor(db, event.session_id)
    if visitor is None:
        event.session_id = str(uuid.uuid4())
        crud.create_visitor(db, event)

    crud.create_event(db, event)

    return {"session_id": event.session_id}


@router.get("/event/page_view", response_model=list[schemas.PageViewSummary])
def get_page_view_summary(db: Session = Depends(get_db)):
    output = crud.get_page_view_summary(db)
    return output

@router.get("/visitor/location")
def get_location(db: Session = Depends(get_db)):
    output = crud.get_visitors_location(db)
    return output


