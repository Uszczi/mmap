import click
from xml.etree import ElementTree as ET
from map_app.models.route import RouteModel, Route
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from map_app.web_app.config import config

@click.group()
def cli():
    pass
engine = create_engine( config.SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

PATH = "/home/mateusz/projects/mmap/data/raw/strava/Evening_Run.gpx"
NAMESPACES = {"":"http://www.topografix.com/GPX/1/1"}

def parse_xml(tree: ET.ElementTree):
    points = []
    root = tree.getroot()
    trk = root.find("trk", namespaces=NAMESPACES)
    for seg in trk.findall("trkseg", namespaces=NAMESPACES):
        for trkpt in seg:
            points.append((trkpt.attrib["lat"], trkpt.attrib["lon"]))
    return points


def _sync():
    tree = ET.parse(PATH)
    points = parse_xml(tree)
    print(points)
    route = Route(points)

    print(route)
    print(route.points)
    model = RouteModel(id=route.id, points=route.points)
    db = SessionLocal()
    db.add(model)
    db.commit()

@cli.command()
def sync():
    _sync()

if __name__ == "__main__":
    _sync()
