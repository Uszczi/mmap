from os import listdir
from pathlib import Path
from xml.etree import ElementTree as ET

from map_app.core.database import get_db
from map_app.models.route import Route, RouteModel
from map_app.shared.routes import ActivityType

NAMESPACES = {"": "http://www.topografix.com/GPX/1/1"}

STRAVA_TYPE_TO_ACTIVITY = {
    "1": ActivityType.BIKE,
    "9": ActivityType.RUN,
    "10": ActivityType.WALK,
    "6": ActivityType.ROLLERBLADE,
}


def save_model(model: RouteModel) -> None:
    with get_db() as db:
        db.add(model)
        db.commit()


def get_path_files() -> list[Path]:
    root = Path(__file__).parent.parent.parent.parent
    strava_dir = root / "data/raw/strava"
    return [strava_dir / name for name in listdir(strava_dir)]


def get_activity_type(tree: ET.ElementTree) -> ActivityType:
    root = tree.getroot()
    trk: ET.Element = root.find("trk", namespaces=NAMESPACES)  # type: ignore
    strava_type: str = trk.find("type", namespaces=NAMESPACES).text  # type: ignore
    activity = STRAVA_TYPE_TO_ACTIVITY[strava_type]
    return activity


def parse_xml(tree: ET.ElementTree):
    points = []
    root = tree.getroot()
    trk: ET.Element = root.find("trk", namespaces=NAMESPACES)  # type: ignore
    for seg in trk.findall("trkseg", namespaces=NAMESPACES):
        for trkpt in seg:
            points.append((float(trkpt.attrib["lat"]), float(trkpt.attrib["lon"])))
    return points


def parse_file(file):
    tree = ET.parse(file)
    points = parse_xml(tree)
    activity = get_activity_type(tree)
    route = Route(points=points, activity=activity)
    print(points)
    model = RouteModel.from_route(route)
    save_model(model)


def load_data():
    for file in get_path_files():
        parse_file(file)

    print("Finished")
