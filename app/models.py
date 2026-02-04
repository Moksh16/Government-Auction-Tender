from app.db import create_db
from app.db import Base
from sqlalchemy import Column, Integer, String,Boolean,DateTime, ForeignKey
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import TIMESTAMP
from enum import Enum, enum
from datetime import Date,datetime

class UserRole(enum.Enum):
    admin = "admin"
    bidder = "bidder"


class BidStatus(enum.Enum):
    accepted = "accepted"
    waiting = "waiting"
    rejected = "rejected"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email_id = Column(String, unique=True, nullable=False, foreign_key= True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    role = Column(Enum(UserRole), nullable=False)
    date_of_birth = Column(Date, nullable=False)

    items_posted = relationship("AuctionItem", back_populates="posted_by_user")
    bids = relationship("Bid", back_populates="bidder")

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, autoincrement=True)
    posted_at = Column(DateTime, default=datetime.utcnow)
    base_price = Column(Integer, nullable=False)
    description = Column(String(500))
    posted_by = Column(String(255), nullable=False)
    time_left = Column(Integer, nullable=False)