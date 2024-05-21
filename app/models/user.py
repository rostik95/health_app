from datetime import datetime, timezone
from sqlalchemy import Float, ForeignKey, String, Integer
from ..extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy.orm import Mapped, mapped_column, relationship


class User(UserMixin, db.Model):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(100), index=True, unique=True)
    email: Mapped[str] = mapped_column(String(150), index=True, unique=True)
    password_hash: Mapped[str] = mapped_column(String(256))
    height_in_cm: Mapped[int] = mapped_column(Integer, nullable=True)

    weights: Mapped[list["Weight"]] = relationship(back_populates="user", cascade="all, delete-orphan")
    
    def __repr__(self) -> str:
        return 'User {}'.format(self.username)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    

class Weight(db.Model):
    __tablename__ = 'weight'
    id: Mapped[int] = mapped_column(primary_key=True)
    value_in_kg: Mapped[float] = mapped_column(Float)
    timestamp: Mapped[datetime] = mapped_column(default=lambda: datetime.now(timezone.utc))

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

    user: Mapped["User"] = relationship(back_populates="weights")