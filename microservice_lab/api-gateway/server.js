const express = require("express");
const cors = require("cors");

const app = express();
app.use(cors());
app.use(express.json());

const PORT = process.env.PORT || 3000;
const USER_SERVICE_URL = process.env.USER_SERVICE_URL || "http://localhost:3001";
const PRODUCT_SERVICE_URL = process.env.PRODUCT_SERVICE_URL || "http://localhost:3002";
const ORDER_SERVICE_URL = process.env.ORDER_SERVICE_URL || "http://localhost:3003";

async function forwardJson(url, res) {
  try {
    const response = await fetch(url);
    const data = await response.json();
    res.status(response.status).json(data);
  } catch (error) {
    res.status(502).json({
      message: "Service unavailable",
      serviceUrl: url,
      error: error.message
    });
  }
}

app.get("/", (req, res) => {
  res.json({
    message: "Microservice Lab API Gateway",
    endpoints: ["/health", "/users", "/products", "/orders", "/orders/summary"]
  });
});

app.get("/health", (req, res) => {
  res.json({
    status: "UP",
    service: "api-gateway",
    userService: USER_SERVICE_URL,
    productService: PRODUCT_SERVICE_URL,
    orderService: ORDER_SERVICE_URL
  });
});

app.get("/users", (req, res) => forwardJson(`${USER_SERVICE_URL}/users`, res));
app.get("/users/:id", (req, res) => forwardJson(`${USER_SERVICE_URL}/users/${req.params.id}`, res));

app.get("/products", (req, res) => forwardJson(`${PRODUCT_SERVICE_URL}/products`, res));
app.get("/products/:id", (req, res) => forwardJson(`${PRODUCT_SERVICE_URL}/products/${req.params.id}`, res));

app.get("/orders", (req, res) => forwardJson(`${ORDER_SERVICE_URL}/orders`, res));
app.get("/orders/summary", (req, res) => forwardJson(`${ORDER_SERVICE_URL}/orders/summary`, res));

app.listen(PORT, () => {
  console.log(`API Gateway running on port ${PORT}`);
});

