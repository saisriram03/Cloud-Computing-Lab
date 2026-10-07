# 🚀 Microservices Lab — FoodFlow

A Dockerized microservices implementation for the Cloud Computing Laboratory.

## Objective
Build a simple distributed food-ordering application using three independent FastAPI microservices:

- 👤 User Service — manages user information
- 🍽️ Restaurant Service — provides restaurant information
- 🧾 Order Service — coordinates an order by communicating with User and Restaurant services

## Architecture

```text
                         Client / Browser / curl
                                  |
                 +----------------+----------------+
                 |                |                |
                 v                v                v
          +-------------+  +-------------+  +-------------+
          | User        |  | Restaurant  |  | Order       |
          | Service     |  | Service     |  | Service     |
          | :8001       |  | :8002       |  | :8003       |
          +-------------+  +-------------+  +------+------+
                                                   |
                                      +------------+------------+
                                      | Docker internal network |
                                      | user-service:8000       |
                                      | restaurant-service:8000 |
                                      +-------------------------+
```

## Project Structure

```text
microservice_lab/
├── docker-compose.yml
├── .gitignore
├── README.md
├── user-service/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── restaurant-service/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
└── order-service/
    ├── app.py
    ├── requirements.txt
    └── Dockerfile
```

## Services

| Service | Host Port | Internal Port | Responsibility |
|---|---:|---:|---|
| User Service | 8001 | 8000 | Returns user details |
| Restaurant Service | 8002 | 8000 | Returns restaurant details |
| Order Service | 8003 | 8000 | Combines user + restaurant data |

## API Endpoints

### User Service
- `GET http://localhost:8001/`
- `GET http://localhost:8001/users/1`

### Restaurant Service
- `GET http://localhost:8002/`
- `GET http://localhost:8002/restaurants/1`

### Order Service
- `GET http://localhost:8003/`
- `GET http://localhost:8003/orders/101`

## Docker Commands

```bash
docker compose up --build
```

Run in background:

```bash
docker compose up --build -d
```

Check containers:

```bash
docker compose ps
```

View logs:

```bash
docker compose logs
```

View individual logs:

```bash
docker compose logs user-service
docker compose logs restaurant-service
docker compose logs order-service
```

Stop everything:

```bash
docker compose down
```

## Testing

Open:

```text
http://localhost:8001/
http://localhost:8001/users/1

http://localhost:8002/
http://localhost:8002/restaurants/1

http://localhost:8003/
http://localhost:8003/orders/101
```

Or:

```bash
curl http://localhost:8003/orders/101
```

## Inter-Service Communication

The Order Service communicates with the other containers using Docker service names:

```text
http://user-service:8000
http://restaurant-service:8000
```

It does not use `localhost:8001` or `localhost:8002` from inside the container because `localhost` refers to the current container.

## Expected Order Response

```json
{
  "order_id": 101,
  "user": {
    "id": 1,
    "name": "Sai Sri Ram",
    "location": "Hubballi"
  },
  "restaurant": {
    "id": 1,
    "name": "Cloud Kitchen Hub",
    "location": "Hubballi",
    "cuisine": "Indian"
  },
  "status": "Confirmed"
}
```

## Why Microservices?

The application is divided into independent services instead of one large application. This gives clear separation of responsibility, independent deployment, easier maintenance, fault isolation, and service-specific scaling.

## Author

**Sai Sri Ram**  
Cloud Computing Laboratory
