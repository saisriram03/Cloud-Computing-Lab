from fastapi import FastAPI, HTTPException

app = FastAPI(title="FoodFlow Restaurant Service", version="1.0")

RESTAURANTS = {
    1: {
        "id": 1,
        "name": "Cloud Kitchen Hub",
        "location": "Hubballi",
        "cuisine": "Indian"
    },
    2: {
        "id": 2,
        "name": "Tech Bites",
        "location": "Dharwad",
        "cuisine": "Multi-Cuisine"
    },
}

@app.get("/")
def root():
    return {"service": "Restaurant Service", "status": "running"}

@app.get("/health")
def health():
    return {"service": "Restaurant Service", "status": "healthy"}

@app.get("/restaurants/{restaurant_id}")
def get_restaurant(restaurant_id: int):
    if restaurant_id not in RESTAURANTS:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return RESTAURANTS[restaurant_id]
