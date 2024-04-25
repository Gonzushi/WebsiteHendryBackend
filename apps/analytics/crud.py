from os import getenv

import pandas as pd
import requests as r
from sqlalchemy.orm import Session

from apps.analytics import models, schemas

API_KEY = getenv("IP_2_LOCATION_API_KEY")


def get_visitor(db: Session, session_id: str):
    return db.get(models.Visitor, session_id)


def create_visitor(db: Session, session_id: str, ip: str) -> schemas.VisitorRead:
    response = r.get(f"https://api.ip2location.io/?key={API_KEY}&ip={ip}")
    data_raw = response.json()
    data_raw["session_id"] = session_id
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


def create_event(db: Session, session_id: str, event: schemas.EventBase):
    print(session_id)
    db_event = models.Event(session_id=session_id, type=event.type, description=event.description)
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

