import json
from os import listdir
from pathlib import Path

from map_app.core.database import get_db
from map_app.models.route import Route, RouteModel
from map_app.shared.routes import ActivityType


def save_model(model: RouteModel) -> None:
    with get_db() as db:
        db.add(model)
        db.commit()


def get_path_files() -> list[Path]:
    root = Path(__file__).parent.parent.parent.parent
    strava_dir = root / "data/raw/endomondo"
    return [strava_dir / name for name in listdir(strava_dir)]


def parse_json(data: dict):
    points = []
    for row in data:
        if "points" in row:
            points_row = row.pop("points")
            for p_row in points_row:
                try:
                    location = p_row[0].pop("location")[0]
                    lat = location[0].pop("latitude")
                    lon = location[1].pop("longitude")
                    points.append((lat, lon))
                except Exception:
                    print("e")
    return points


def parse_file(file):
    with open(file) as f:
        data = json.load(f)
        points = parse_json(data)
        route = Route(points=points, activity=ActivityType.RUN)
        model = RouteModel.from_route(route)
        save_model(model)


def load_data():
    for file in get_path_files():
        parse_file(file)

    print("Finished")
