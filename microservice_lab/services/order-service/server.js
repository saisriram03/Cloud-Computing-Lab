const express = require("express");
const cors = require("cors");
const orders = require("./data/orders.json");

const app = express();
app.use(cors());
app.use(express.json());

const PORT = process.env.PORT || 3003;
const USER_SERVICE_URL = process.env.USER_SERVICE_URL || "http://localhost:3001";
const PRODUCT_SERVICE_URL = process.env.PRODUCT_SERVICE_URL || "http://localhost:3002";

async function getJson(url) {
  const response = await fetch(url);

  if (!response.ok) {
    throw new Error(`Request failed: ${url}`);
  }

  return response.json();
}

app.get("/health", (req, res) => {
  res.json({ status: "UP", service: "order-service" });
});

app.get("/orders", (req, res) => {
  res.json(orders);
});

app.get("/orders/summary", async (req, res) => {
  try {
    const summary = await Promise.all(
      orders.map(async (order) => {
        const user = await getJson(`${USER_SERVICE_URL}/users/${order.userId}`);
        const product = await getJson(`${PRODUCT_SERVICE_URL}/products/${order.productId}`);

        return {
          orderId: order.id,
          quantity: order.quantity,
          user: user.name,
          product: product.name,
          totalAmount: product.price * order.quantity
        };
      })
    );

    res.json(summary);
  } catch (error) {
    res.status(502).json({
      message: "Unable to build order summary",
      error: error.message
    });
  }
});

app.listen(PORT, () => {
  console.log(`Order Service running on port ${PORT}`);
});

