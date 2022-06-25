from fastapi import APIRouter

from typing import List
from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware
from xml.etree import ElementTree as ET
from map_app.models.route import RouteModel, Route
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from map_app.web_app.config import config
from map_app.models import RouteModel
from map_app.models.route import Route

router = APIRouter()

@router.get("/routes")
def get_all_routes() -> list[Route]:
    engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    models = db.query(RouteModel).all()
    print(models)
    mm = [Route(model.points) for model in models]
    return mm
