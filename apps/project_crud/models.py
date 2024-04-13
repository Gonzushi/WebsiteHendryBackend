from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Brand(Base):
    __tablename__ = "brand"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), unique=True, index=True)

    products: Mapped[list["Product"]] = relationship(back_populates="brand")

    def __repr__(self) -> str:
        return f"Brand(id={self.id!r}, name={self.name!r})"


class Product(Base):
    __tablename__ = "product"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    description: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    price: Mapped[int] = mapped_column()
    brand_id: Mapped[int | None] = mapped_column(
        ForeignKey("brand.id", ondelete="NO ACTION"), nullable=True
    )

    brand: Mapped["Brand"] = relationship(back_populates="products")

    def __repr__(self) -> str:
        return f"Brand(id={self.id!r}, name={self.name!r}, description={self.description!r}, price={self.price!r}, brand_id={self.brand_id!r})"
