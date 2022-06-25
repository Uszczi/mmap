from fastapi import APIRouter

from map_app.routers.route import router as route_router

router = APIRouter(prefix="/api")

router.include_router(route_router)
