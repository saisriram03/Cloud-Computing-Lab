import os
import requests
from fastapi import FastAPI, HTTPException

app = FastAPI(title="FoodFlow Order Service", version="1.0")

USER_SERVICE_URL = os.getenv("USER_SERVICE_URL", "http://user-service:8000")
RESTAURANT_SERVICE_URL = os.getenv(
    "RESTAURANT_SERVICE_URL", "http://restaurant-service:8000"
)

@app.get("/")
def root():
    return {"service": "Order Service", "status": "running"}

@app.get("/health")
def health():
    return {"service": "Order Service", "status": "healthy"}

@app.get("/orders/{order_id}")
def get_order(order_id: int):
    if order_id != 101:
        raise HTTPException(status_code=404, detail="Order not found")

    user_response = requests.get(f"{USER_SERVICE_URL}/users/1", timeout=5)
    restaurant_response = requests.get(
        f"{RESTAURANT_SERVICE_URL}/restaurants/1", timeout=5
    )

    if user_response.status_code != 200:
        raise HTTPException(status_code=502, detail="User Service unavailable")

    if restaurant_response.status_code != 200:
        raise HTTPException(
            status_code=502, detail="Restaurant Service unavailable"
        )

    return {
        "order_id": order_id,
        "user": user_response.json(),
        "restaurant": restaurant_response.json(),
        "status": "Confirmed",
    }
