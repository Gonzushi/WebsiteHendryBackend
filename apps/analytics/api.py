import uuid

from fastapi import APIRouter, Depends, Request, Response
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
    event: schemas.EventBase,
    request: Request,
    response: Response,
    db: Session = Depends(get_db),
):
    if "session_id" in request.cookies:
        session_id = request.cookies["session_id"]
        visitor: models.Visitor = crud.get_visitor(db, session_id)
        if visitor is None:
            session_id = None
        else:
            session_id = visitor.session_id
    else:
        session_id = None

    if session_id is None:
        session_id = str(uuid.uuid4())
        crud.create_visitor(db, session_id, event.ip_address)
        response.set_cookie(
            key="session_id", value=session_id, max_age=365 * 24 * 60 * 60
        )

    crud.create_event(db, session_id, event)
