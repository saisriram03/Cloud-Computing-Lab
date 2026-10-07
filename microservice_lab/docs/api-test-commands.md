# API Test Commands

Start the application:

```bash
docker compose up --build
```

Test API Gateway:

```bash
curl http://localhost:3000
curl http://localhost:3000/health
```

Test User Service through gateway:

```bash
curl http://localhost:3000/users
curl http://localhost:3000/users/1
```

Test Product Service through gateway:

```bash
curl http://localhost:3000/products
curl http://localhost:3000/products/101
```

Test Order Service through gateway:

```bash
curl http://localhost:3000/orders
curl http://localhost:3000/orders/summary
```

Stop containers:

```bash
docker compose down
```

