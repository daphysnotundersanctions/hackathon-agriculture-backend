import express from "express";
import cors from "cors";
import bodyParser from "body-parser";
import { Sequelize } from "sequelize";

import { db } from "./db.js";

const app = express();
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
const port = 3000;

// import { EmployeeModel } from "./models/employee.js";
import { Plants } from "./models/plants.js";

app.post("/postPlantInfo", async (req, res) => {
  //   Plants.sync().then(() => {
  //     console.log("User model is sync");
  //   });
  // await.
  if (!req.body) return res.sendStatus(400);
  let plantTemp = req.body.plantTemp;
  let plantWet = req.body.plantWet;
  await Plants.create({
    temp: plantTemp,
    wet: plantWet,
  })
    .then(() => res.status(200).send("Информация добавилась"))
    .catch((e) => {
      res.status(500).send(e);
    });
});

app.get("/", (req, res) => {
  res.send("Hello World!");
});

db.sync()
  .then(() => {
    app.listen(port, function () {
      console.log("Сервер ожидает подключения...");
    });
  })
  .catch((err) => console.log(err));
