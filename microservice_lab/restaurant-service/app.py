from fastapi import FastAPI


app = FastAPI(title="Restaurant Service")


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
        "name": "Sai Food Palace",
        "location": "Hubballi",
        "cuisine": "Indian"
    }

