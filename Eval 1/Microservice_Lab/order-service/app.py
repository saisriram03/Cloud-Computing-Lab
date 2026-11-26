from fastapi import FastAPI
import requests

app = FastAPI(title="Sai Food Delivery - Order Service")


@app.get("/")
def home():
    return {
        "service": "Order Service",
        "status": "running"
    }


@app.get("/orders/{order_id}")
def get_order(order_id: int):

    # Call User Service
    user_response = requests.get(
        "http://user-service:8000/users/1"
    )

    # Call Restaurant Service
    restaurant_response = requests.get(
        "http://restaurant-service:8000/restaurants/1"
    )

    # Convert responses to JSON
    user = user_response.json()
    restaurant = restaurant_response.json()

    # Return combined order information
    return {
        "order_id": order_id,
        "user": user,
        "restaurant": restaurant,
        "status": "Confirmed"
    }