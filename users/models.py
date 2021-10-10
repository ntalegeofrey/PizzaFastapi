from config.database import Base
from sqlalchemy import Column, Integer, Boolean, Text, String, ForeignKey
from sqlalchemy.orm import relationship
from orders.models import Order


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String(25), unique=True)
    email = Column(String(80), unique=True)
    password = Column(Text, nullable=True)
    is_staff = Column(Boolean, default=False)
    is_active = Column(Boolean, default=False)
    orders = relationship(Order, back_populates="user")

    def __repr__(self):
        return f"<User {self.username}"
