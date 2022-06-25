from typing import List
from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware
from xml.etree import ElementTree as ET
from map_app.models.route import RouteModel, Route
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from map_app.web_app.config import config
from map_app.routers.main import router
app = FastAPI()

@app.get("/")
def hello_world():
    return {"hhjhjello":"world"}

origins = [
    "http://localhost",
    "http://localhost:8080",
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
