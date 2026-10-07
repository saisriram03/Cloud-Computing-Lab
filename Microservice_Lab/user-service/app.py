from fastapi import FastAPI

app = FastAPI(title="Sai Food Delivery - User Service")


@app.get("/")
def home():
    return {
        "service": "User Service",
        "status": "running"
    }


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "id": user_id,
        "name": "Sai Sri Ram",
        "location": "Hubballi"
    }