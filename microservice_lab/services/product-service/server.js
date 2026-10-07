const express = require("express");
const cors = require("cors");
const products = require("./data/products.json");

const app = express();
app.use(cors());
app.use(express.json());

const PORT = process.env.PORT || 3002;

app.get("/health", (req, res) => {
  res.json({ status: "UP", service: "product-service" });
});

app.get("/products", (req, res) => {
  res.json(products);
});

app.get("/products/:id", (req, res) => {
  const product = products.find((item) => item.id === Number(req.params.id));

  if (!product) {
    return res.status(404).json({ message: "Product not found" });
  }

  res.json(product);
});

app.listen(PORT, () => {
  console.log(`Product Service running on port ${PORT}`);
});

