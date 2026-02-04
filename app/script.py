from fastapi import FastAPI, Response,status,HTTPException, Depends, APIRouter
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional, List
from random import randrange
from passlib.context import CryptContext
import psycopg2
from psycopg2.extras import RealDictCursor
import time

from app import auth, schemas,models,utils
from app.db import engine, SessionLocal, get_db
from sqlalchemy.orm import Session
app = FastAPI()

app.include_router(auth.router)
