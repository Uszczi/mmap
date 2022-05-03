from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello_world():
    return {"hhjhjello":"world"}


from map_app.models import Item
