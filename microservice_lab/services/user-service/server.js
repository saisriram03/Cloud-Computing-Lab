const express = require("express");
const cors = require("cors");
const users = require("./data/users.json");

const app = express();
app.use(cors());
app.use(express.json());

const PORT = process.env.PORT || 3001;

app.get("/health", (req, res) => {
  res.json({ status: "UP", service: "user-service" });
});

app.get("/users", (req, res) => {
  res.json(users);
});

app.get("/users/:id", (req, res) => {
  const user = users.find((item) => item.id === Number(req.params.id));

  if (!user) {
    return res.status(404).json({ message: "User not found" });
  }

  res.json(user);
});

app.listen(PORT, () => {
  console.log(`User Service running on port ${PORT}`);
});

