from attr import asdict
from fastapi import APIRouter

from map_app.core.database import get_db
from map_app.models import RouteModel
from map_app.models.route import RouteModel

router = APIRouter()


@router.get("/routes")
def get_all_routes() -> list[dict]:
    with get_db() as db:
        models = db.query(RouteModel).all()
        print(models)

    routes = [asdict(model.to_route_()) for model in models]

    return routes
