from sqlalchemy import ForeignKey, String, Integer
from ..extensions import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
from datetime import datetime, timezone


if TYPE_CHECKING:
    from .user import User


class Food(db.Model):
    __tablename__ = 'food'
    id: Mapped[int] = mapped_column(primary_key=True)
    photo: Mapped[str] = mapped_column(String)
    name: Mapped[str] = mapped_column(String(150))
    kcal: Mapped[int] = mapped_column(Integer)
    proteins: Mapped[int] = mapped_column(Integer)
    fats: Mapped[int] = mapped_column(Integer)
    carbs: Mapped[int] = mapped_column(Integer)

    ingestions: Mapped[list["Ingestion"]] = relationship(back_populates="food", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f'{self.name!r}'
    

class Ingestion(db.Model):
    __tablename__ = 'ingestion'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    food_id: Mapped[int] = mapped_column(ForeignKey("food.id"))
    grams: Mapped[int] = mapped_column(Integer)
    timestamp: Mapped[datetime] = mapped_column(default=lambda: datetime.now(timezone.utc))

    user: Mapped["User"] = relationship(back_populates="ingestions")
    food: Mapped["Food"] = relationship(back_populates="ingestions")

    def __repr__(self) -> str:
        return f"{self.user!r} ate {self.grams!r} of {self.food!r}"