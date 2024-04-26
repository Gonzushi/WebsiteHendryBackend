import datetime
from sqlalchemy import ForeignKey, String, DateTime, Column
from sqlalchemy.dialects import mssql
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    created_at = Column(DateTime, default=datetime.datetime.now(datetime.UTC))


class Visitor(Base):
    __tablename__ = "visitors"

    session_id: Mapped[str] = mapped_column(String(255), primary_key=True)
    ip_address: Mapped[str] = mapped_column(String(15))
    country_code: Mapped[str] = mapped_column(String(255))
    country_name: Mapped[str] = mapped_column(String(255))
    region_name: Mapped[str] = mapped_column(String(255))
    city_name: Mapped[str] = mapped_column(String(255))
    latitude: Mapped[float] = mapped_column(mssql.FLOAT(6))
    longitude: Mapped[float] = mapped_column(mssql.FLOAT(6))
    zip_code: Mapped[int] = mapped_column(mssql.INTEGER)
    time_zone: Mapped[str] = mapped_column(String(255))
    asn: Mapped[str] = mapped_column(String(255))
    asn_name: Mapped[str] = mapped_column(String(255))
    is_proxy: Mapped[str] = mapped_column(String(255))


class Event(Base):
    __tablename__ = "events"

    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=False)
    ip_address: Mapped[str] = mapped_column(String(15))
    session_id: Mapped[str] = mapped_column(
        ForeignKey("visitors.session_id"), nullable=False
    )
