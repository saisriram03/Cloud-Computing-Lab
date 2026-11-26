from fastapi import FastAPI

app = FastAPI(title="Sai Food Delivery - Restaurant Service")


@app.get("/")
def home():
    return {
        "service": "Restaurant Service",
        "status": "running"
    }


@app.get("/restaurants/{restaurant_id}")
def get_restaurant(restaurant_id: int):
    return {
        "id": restaurant_id,
        "name": "Sai Food Hub",
        "location": "Hubballi",
        "cuisine": "Indian"
    }