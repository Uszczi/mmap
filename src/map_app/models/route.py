from inspect import isclass
from typing import Tuple
from uuid import uuid4
from pydantic.types import UUID4
from sqlalchemy.sql.sqltypes import Text
from .base import Base
from sqlalchemy import Column, Integer, String

from sqlalchemy.dialects.postgresql import UUID
class RouteModel(Base):
    __tablename__ = "routes"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    points = Column(Text)


class Route:
    def __init__(self, points: str | Tuple[float, float], id = None):
        if id is None:
            self.id= uuid4()

        if type(points) == str:
            self.points = []
            points = points.split("|")
            for point in points:
                lat, lon = point.split(",")
                self.points.append((lat,lon))

        else:
            self.points = ""
            for point in points:
                self.points += f"{point[0]},{point[1]}|"
            self.points = self.points[:-1]
