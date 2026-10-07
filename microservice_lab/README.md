# Microservice Lab

This lab demonstrates a small cloud-ready microservice application using Node.js, Express, Docker, Docker Compose, and Kubernetes manifests.

## Aim

To design, build, containerize, and deploy a simple microservice-based application where independent services communicate through REST APIs.

## Services

| Service | Port | Responsibility |
| --- | --- | --- |
| API Gateway | 3000 | Single entry point for clients |
| User Service | 3001 | Maintains user details |
| Product Service | 3002 | Maintains product catalog |
| Order Service | 3003 | Maintains order details and combines data from other services |

## Project Structure

```text
microservice_lab/
  api-gateway/
  services/
    user-service/
    product-service/
    order-service/
  kubernetes/
  docs/
  screenshots/
  docker-compose.yml
  .env.example
```

## Requirements

- Node.js 18 or later
- Docker Desktop
- Kubernetes or Minikube
- kubectl
- Postman or curl

## Run With Docker Compose

```bash
docker compose up --build
```

Open the health endpoint:

```bash
curl http://localhost:3000/health
```

## Main API Endpoints

```bash
curl http://localhost:3000/users
curl http://localhost:3000/products
curl http://localhost:3000/orders
curl http://localhost:3000/orders/summary
```

## Run Locally Without Docker

Open four terminals and run:

```bash
cd services/user-service
npm install
npm start
```

```bash
cd services/product-service
npm install
npm start
```

```bash
cd services/order-service
npm install
npm start
```

```bash
cd api-gateway
npm install
npm start
```

## Kubernetes Deployment

```bash
kubectl apply -f kubernetes/namespace.yaml
kubectl apply -f kubernetes/configmap.yaml
kubectl apply -f kubernetes/user-service.yaml
kubectl apply -f kubernetes/product-service.yaml
kubectl apply -f kubernetes/order-service.yaml
kubectl apply -f kubernetes/api-gateway.yaml
```

Check pods and services:

```bash
kubectl get pods -n microservice-lab
kubectl get svc -n microservice-lab
```

## Result

The microservice application was successfully designed with separate services, containerized using Docker, composed using Docker Compose, and prepared for Kubernetes deployment.

