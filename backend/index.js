const express = require("express");
const cors = require("cors");

const app = express();
app.use(express.json());
app.use(cors({ origin: true }));

app.post("/authenticate", async (res, req) => {
  const { username } = req.body;
  return res.json({ username: username, secret: "sha256..." });
});

app.listen(3001)
