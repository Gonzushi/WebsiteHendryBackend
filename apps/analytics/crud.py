import pandas as pd
import requests as r
from sqlalchemy.orm import Session
from sqlalchemy.sql import text

from apps.analytics import models, schemas
from apps.env import API_KEY


def get_visitor(db: Session, session_id: str) -> schemas.Visitor:
    return db.get(models.Visitor, session_id)


def create_visitor(db: Session, event: schemas.Event) -> schemas.Visitor:
    response = r.get(f"https://api.ip2location.io/?key={API_KEY}&ip={event.ip_address}")
    data_raw = response.json()
    print("-" * 10, data_raw)
    data_raw["session_id"] = event.session_id
    data_raw["ip_address"] = data_raw["ip"]
    data_raw["zip_code"] = int(data_raw["zip_code"])
    data_raw["is_proxy"] = str(data_raw["is_proxy"])
    data_raw["asn_name"] = str(data_raw["as"])
    data_raw.pop("ip")
    data_raw.pop("as")

    db_visitor = models.Visitor(**data_raw)
    db.add(db_visitor)
    db.commit()
    db.refresh(db_visitor)
    return db_visitor


def create_event(db: Session, event: schemas.Event):
    db_event = models.Event(**event.model_dump())
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event


def get_page_view_summary(db: Session) -> list[schemas.PageViewSummary]:
    statement = text(
        """select description, COUNT(*) from events group by description"""
    )
    data = db.execute(statement)
    df = pd.DataFrame(data.all(), columns=data.keys())
    df.rename(columns={"description": "path", "": "total"}, inplace=True)
    output = df.to_dict("records")
    return output
