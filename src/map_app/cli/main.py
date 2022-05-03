import click
from xml.etree import ElementTree as ET

@click.group()
def cli():
    pass


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


@cli.command()
def sync():
    _sync()

if __name__ == "__main__":
    _sync()
