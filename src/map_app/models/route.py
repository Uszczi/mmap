from __future__ import annotations

from uuid import uuid4

from attr import define, ib
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.sqltypes import Text

from map_app.shared.routes import ActivityType

from .base import Base


class RouteModel(Base):
    __tablename__ = "routes"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    points = Column(Text)
    activity = Column(Text)

    @classmethod
    def from_route(cls, route: Route) -> RouteModel:
        points = ""
        for point in route.points:
            points += f"{point[0]},{point[1]}|"
        points = points[:-1]

        return cls(id=route.id, points=points, activity=route.activity)  # type: ignore

    def to_route(self):
        points = []
        splited_points = self.points.split("|")
        for point in splited_points:
            lat, lon = point.split(",")
            points.append((float(lat), float(lon)))

        return Route(id=self.id, activity=ActivityType(self.activity), points=points)  # type: ignore

    def to_route_(self) -> Route:
        points = []
        splited_points = self.points.split("|")
        for i, point in enumerate(splited_points):
            if i % 10 != 1: continue

            lat, lon = point.split(",")
            points.append((float(lat), float(lon)))

        return Route(id=self.id, activity=ActivityType(self.activity), points=points)  # type: ignore

@define(kw_only=True)
class Route:
    id: UUID = ib(factory=uuid4)
    activity: ActivityType
    points: list[tuple[float, float]]
