# 🍱 FOOD DELIVERY — Containerized Microservice Application

<div align="center">

![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-REST%20API-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Compose](https://img.shields.io/badge/Docker%20Compose-Orchestration-0DB7ED?style=for-the-badge&logo=docker&logoColor=white)

### 🚀 Cloud Computing Lab • Microservices • Docker • Performance Analysis

**Prepared by: Sai Sri Ram**

</div>

> 💡 **Project Theme:** A lightweight food-delivery system built as three independent REST microservices, containerized with Docker and evaluated under increasing concurrent workloads.

---

## 1. Experiment Overview

This experiment demonstrates the development, deployment, and performance analysis of a containerized microservice application under varying workloads.

The application consists of three independent microservices. Each microservice provides a REST API and is independently containerized using Docker. Docker Compose is used to deploy the complete application and establish communication between the services through a common Docker network.

## 2. Aim

To develop a microservice-based application containing three independent services, containerize and deploy the services using Docker, establish inter-service communication, generate varying workloads, monitor resource utilization, and analyze application performance.

## 3. Application Architecture

```text
                         CLIENT
                            |
                            v
                   +----------------+
                   |  ORDER SERVICE |
                   |    Port 8003   |
                   +--------+-------+
                            |
                     Docker Network
                       /          \
                      /            \
                     v              v
            +---------------+   +--------------------+
            | USER SERVICE  |   | RESTAURANT SERVICE |
            |   Port 8001   |   |     Port 8002      |
            +---------------+   +--------------------+
```
## 🧰 2. Technologies Used

- Python 3.13
- FastAPI for REST APIs
- Docker
- Docker Compose
- Python `urllib`
- Python `ThreadPoolExecutor`
- Docker `stats` for CPU and memory monitoring
- Git
- GitHub

## 🖥️ 3. Test Environment

- OS: Windows with PowerShell
- Python: Python 3.13
- Docker Desktop
- Docker Compose
- Three Docker containers
- REST-based microservice architecture


## 🧩 5. Microservices

| **Service** | **Port** | **Responsibility** |
|-------------|----------|--------------------|
| user-service | 8001 | Stores and returns user information |
| restaurant-service | 8002 | Stores and returns restaurant information |
| order-service | 8003 | Processes orders and communicates with User and Restaurant services |

---

### 5.1 user-service (Port 8001)

| **Endpoint** | **Description** |
|--------------|-----------------|
| GET `/users/1` | Returns user information |

---

### 5.2 restaurant-service (Port 8002)

| **Endpoint** | **Description** |
|--------------|-----------------|
| GET `/restaurants/1` | Returns restaurant information |

---

### 5.3 order-service (Port 8003)

| **Endpoint** | **Description** |
|--------------|-----------------|
| GET `/orders/1` | Retrieves order information and communicates with User and Restaurant services |

---
5.4 Example End-to-End Response

The Order Service combines information obtained from the User Service and Restaurant Service.
```
{
    "order_id": 1,
    "user": {
        "id": 1,
        "name": "Sai Sri Ram"
    },
    "restaurant": {
        "id": 1,
        "name": "Sai Food Hub"
    },
    "status": "Confirmed"
}

```
6. Project Structure :
```
microservice_lab/
|
|-- user-service/
|   |-- main.py
|   |-- requirements.txt
|   |-- Dockerfile
|
|-- restaurant-service/
|   |-- main.py
|   |-- requirements.txt
|   |-- Dockerfile
|
|-- order-service/
|   |-- main.py
|   |-- requirements.txt
|   |-- Dockerfile
|
|-- docker-compose.yml
|-- load_test.py
|-- README.md
```

## 🛠️ 7. Checkpoint 1 - Design and Develop the Microservices

1. Domain selected: Food Delivery.
2. Three independent microservices were identified:
   - User Service
   - Restaurant Service
   - Order Service
3. Responsibility of each service was defined.
4. Services were implemented using Python and FastAPI.
5. REST API endpoints were created for every service.
6. Each service was tested independently.
7. All APIs returned successful responses.

### User Service

The User Service is responsible for providing user information.

### Restaurant Service

The Restaurant Service is responsible for providing restaurant information.

### Order Service

The Order Service is responsible for processing orders and communicating with the User and Restaurant services.

---

## 🐳 8. Checkpoint 2 - Containerize and Deploy

1. A separate Dockerfile was created for each service.
2. Each service contains its own `requirements.txt`.
3. Docker images were built for all three services.
4. Docker images were verified.
5. `docker-compose.yml` was created.
6. All three services were configured in Docker Compose.
7. The application was deployed using Docker Compose.
8. All three containers were verified as running.

### Build and Start

```powershell
docker compose up -d --build
```
Verify Containers 
```
docker compose ps
```
## 🔗 9. Checkpoint 3 - Microservice Communication

The three services communicate through the Docker Compose network.

The communication flow is:
```
Client
   |
   | GET /orders/1
   v
Order Service
   |
   +------> User Service
   |
   +------> Restaurant Service
   |
   v
Combined Order Response
```
The Order Service communicates with the User Service and Restaurant Service and combines their responses.

Main End-to-End API
```
http://localhost:8003/orders/1
```
The request successfully returned a combined response containing:

1.Order information
2.User information
3.Restaurant information
4.Order status

This confirms successful inter-service communication.

## 📈 10. Checkpoint 4 - Workload Generation and Monitoring
    
1.API selected for testing: GET /orders/1
2.A custom Python load-testing script was created.
3.ThreadPoolExecutor was used for concurrent requests.
4.Five workload levels were tested.
5.Workload levels were:
-concurrent request
-2concurrent requests
-4 concurrent requests
-8 concurrent requests
-16 concurrent requests
6.Each workload generated 20 requests.
7.Average response time was measured.
8.Throughput was calculated.
9.Successful and failed requests were counted.
10.CPU and memory utilization were monitored using Docker Stats.

Run Load Test
```
py -3.13 load_test.py
```
Monitor Docker Resources
```
docker stats --no-stream
```

## 📊 11. Checkpoint 5 - Results and Analysis

### 11.1 Observation Table

| **Workload** | **Concurrency** | **Total Requests** | **Successful** | **Failed** | **Avg Response Time (s)** | **Total Test Time (s)** | **Throughput (req/s)** |
|--------------|-----------------|--------------------|----------------|------------|----------------------------|--------------------------|------------------------|
| W1 | 1 | 20 | 20 | 0 | 0.0212 | 0.4282 | 46.71 |
| W2 | 2 | 20 | 20 | 0 | 0.0269 | 0.2759 | 72.48 |
| W3 | 4 | 20 | 20 | 0 | 0.0328 | 0.1783 | 112.19 |
| W4 | 8 | 20 | 20 | 0 | 0.0605 | 0.1696 | 117.94 |
| W5 | 16 | 20 | 20 | 0 | 0.0717 | 0.1303 | 153.54 |

---

### 11.2 CPU Utilization

| **Service** | **Observed CPU Utilization** |
|-------------|------------------------------|
| order-service | Approximately 0.18% - 0.20% |
| user-service | Approximately 0.24% - 0.31% |
| restaurant-service | Approximately 0.21% - 0.28% |



---

### 11.3 Memory Utilization

| **Service** | **Observed Memory Utilization** |
|-------------|---------------------------------|
| order-service | Approximately 42.6 - 42.8 MiB |
| user-service | Approximately 36.7 - 36.8 MiB |
| restaurant-service | Approximately 35.2 - 35.7 MiB |

---

### 11.4 Performance Observation Table

| **Workload** | **Concurrency** | **Avg Response Time (s)** | **Throughput (req/s)** | **Failed Requests** |
|--------------|-----------------|----------------------------|------------------------|---------------------|
| W1 | 1 | 0.0212 | 46.71 | 0 |
| W2 | 2 | 0.0269 | 72.48 | 0 |
| W3 | 4 | 0.0328 | 112.19 | 0 |
| W4 | 8 | 0.0605 | 117.94 | 0 |
| W5 | 16 | 0.0717 | 153.54 | 0 |

### 11.5 Workload Summary

| Workload | Concurrency | Response Time | Throughput | Failed Requests | Success Rate |
|---|---:|---:|---:|---:|---:|
| W1 | 1 | 0.0212 s | 46.71 req/s | 0 | 100% |
| W2 | 2 | 0.0269 s | 72.48 req/s | 0 | 100% |
| W3 | 4 | 0.0328 s | 112.19 req/s | 0 | 100% |
| W4 | 8 | 0.0605 s | 117.94 req/s | 0 | 100% |
| W5 | 16 | 0.0717 s | 153.54 req/s | 0 | 100% |


### 11.6 Concurrent Requests vs Average Response Time

| Concurrent Requests | Average Response Time (s) |
|---:|---:|
| 1 | 0.0212 |
| 2 | 0.0269 |
| 4 | 0.0328 |
| 8 | 0.0605 |
| 16 | 0.0717 |

### 11.7 Concurrent Requests vs Throughput

| Concurrent Requests | Throughput (req/s) |
|---:|---:|
| 1 | 46.71 |
| 2 | 72.48 |
| 4 | 112.19 |
| 8 | 117.94 |
| 16 | 153.54 |

### 11.8 Docker Resource Snapshot

| Service | CPU Snapshot | Memory Snapshot |
|---|---:|---:|
| order-service | 0.18% - 0.20% | 42.6 - 42.8 MiB |
| user-service | 0.24% - 0.31% | 36.7 - 36.8 MiB |
| restaurant-service | 0.21% - 0.28% | 35.2 - 35.7 MiB |

### 11.9 Final Performance Summary

| Metric | Result |
|---|---:|
| Total Requests Tested | 100 |
| Successful Requests | 100 |
| Failed Requests | 0 |
| Success Rate | 100% |
| Maximum Throughput | 153.54 req/s |
| Maximum Tested Concurrency | 16 |
| Minimum Response Time | 0.0212 s |
| Maximum Response Time | 0.0717 s |
| Highest Observed CPU | 0.31% |
| Highest Observed Memory | 42.8 MiB |
| Service With Highest Observed Memory | order-service ||

### 11.10 Overall Test Summary

| **Parameter** | **Result** |
|---------------|------------|
| Number of Microservices | 3 |
| Workload Levels | 5 |
| Concurrency Levels | 1, 2, 4, 8, 16 |
| Requests per Workload | 20 |
| Total Requests | 100 |
| Successful Requests | 100 |
| Failed Requests | 0 |
| Success Rate | 100% |
| Maximum Throughput | 153.54 req/s |
| Maximum Concurrency | 16 |
| Lowest Response Time | 0.0212 s |
| Highest Response Time | 0.0717 s |
| Highest Observed Memory | Order Service |

## ▶️ 12. How to Run

For anyone cloning this repository:
```
git clone https://github.com/saisriram03/Cloud-Computing-Lab.git
cd Cloud-Computing-lab/microservice_lab
docker compose up -d --build
docker compose ps
```
Test the main API:
```
http://localhost:8003/orders/1
```
Run the load test:
```
py -3.13 load_test.py
```
Monitor Docker resources:
```
docker stats --no-stream
```
## 🛑 13. Stop the Application

To stop all services:
```
docker compose down
```
---

## 🎨 Performance Graphs

### Response Time vs Concurrent Requests

The graph below shows how the average response time changes as the number of concurrent requests increases.

![Response Time vs Concurrent Requests](screenshots/response_time_vs_concurrency.png)

### Throughput vs Concurrent Requests

The graph below shows the throughput achieved at different concurrency levels.

![Throughput vs Concurrent Requests](screenshots/throughput_vs_concurrency.png)

## ✅ 14. Final Deliverables Checklist

- [x] Source code of the three microservices
- [x] Three Dockerfiles
- [x] Three requirements files
- [x] `docker-compose.yml`
- [x] Running Docker containers
- [x] REST API endpoints
- [x] Inter-service communication
- [x] End-to-end API testing
- [x] Workload testing
- [x] Response-time measurements
- [x] Throughput measurements
- [x] Successful and failed request measurements
- [x] CPU monitoring using Docker Stats
- [x] Memory monitoring using Docker Stats
- [x] Performance observation table
- [x] Performance analysis
- [x] Conclusion
- [x] GitHub repository

---

## 🔗 15. GitHub Repository

**Repository:**

https://github.com/saisriram03/Cloud-Computing-Lab

**Microservice Lab:**

```text
Cloud-Computing-lab/
└── microservice_lab/
```
## 🔄 16. Experiment Workflow
```
DEVELOP
   ↓
3 Independent Microservices
   ↓
CONTAINERIZE
   ↓
Dockerfiles
   ↓
DEPLOY
   ↓
Docker Compose
   ↓
CONNECT
   ↓
Inter-Service Communication
   ↓
LOAD TEST
   ↓
1, 2, 4, 8, 16 Concurrent Requests
   ↓
MONITOR
   ↓
CPU and Memory
   ↓
ANALYZE
   ↓
Response Time and Throughput
   ↓
DEMONSTRATE
   ↓
GitHub
```
