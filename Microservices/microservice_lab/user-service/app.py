from fastapi import FastAPI, HTTPException

app = FastAPI(title="FoodFlow User Service", version="1.0")

USERS = {
    1: {"id": 1, "name": "Sai Sri Ram", "location": "Hubballi"},
    2: {"id": 2, "name": "Cloud User", "location": "Dharwad"},
}

@app.get("/")
def root():
    return {"service": "User Service", "status": "running"}

@app.get("/health")
def health():
    return {"service": "User Service", "status": "healthy"}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id not in USERS:
        raise HTTPException(status_code=404, detail="User not found")
    return USERS[user_id]
