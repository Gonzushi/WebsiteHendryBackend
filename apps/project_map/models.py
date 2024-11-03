from sqlalchemy import Float, String, Integer, Numeric, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Location(Base):
    __tablename__ = "location"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, unique=True)
    latitude: Mapped[float] = mapped_column(Numeric(30, 26), nullable=False)  
    longitude: Mapped[float] = mapped_column(Numeric(31, 26), nullable=False)  
    phone_number: Mapped[str] = mapped_column(String(255), nullable=True)
    area: Mapped[int] = mapped_column(Integer, nullable=True)
    type: Mapped[str] = mapped_column(String(255), nullable=True)
    price: Mapped[float] = mapped_column(Float, nullable=True)
    comment: Mapped[str] = mapped_column(Text, nullable=True) 

    def __repr__(self) -> str:
        return (
            f"Location(id={self.id!r}, latitude={self.latitude!r}, "
            f"longitude={self.longitude!r}, phone_number={self.phone_number!r}, "
            f"area={self.area!r}, type={self.type!r}, price={self.price!r}, "
            f"comment={self.comment!r})"
        )
