from fastapi import pydantic
from pydantic import Base, EmailStr
from typing import Optional
from datetime import date

class UserSigin(Base):
    Email_id: EmailStr
    Username: str
    Password: str
    Role: str
    DateOfBirth: date

class Post_new_item(Base):
    title:str
    description: str
    posted_by: EmailStr
    id: int
    time_duration:int
    base_price: int

class Items(Base):
    posted_at : date
    Base_price: int
    description: str
    posted_by: str
    time_left: str
    id: int

class Bids(Base):
    name: str
    posted_at: date
    bidder_id: int
    posted_by: str
    amount: int

class Bids_info(Base):
    name: str
    Posted_at: date
    Base_price: int
    description: str
    time_duration: int
    status: str