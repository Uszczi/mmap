from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from map_app.routers.main import router

app = FastAPI(
    docs_url="/api/docs", redoc_url="/api/redoc", openapi_url="/api/openapi.json"
)


@app.get("/")
def hello_world():
    return {"hhjhjello": "world"}


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
