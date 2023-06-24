import express from "express";
import cors from "cors";
import bodyParser from "body-parser";

import { db } from "./db.js";

const app = express();
app.use(bodyParser.json());
const urlencodedParser = express.urlencoded({ extended: false });
const port = 3000;

db.sync()
  .then(() => {
    app.listen(port, function () {
      console.log("Сервер ожидает подключения...");
    });
  })
  .catch((err) => console.log(err));
// import { EmployeeModel } from "./models/employee.js";
import { Plants } from "./models/plants.js";

app.get("/", (req, res) => {
  res.send("Hello World!");
});

app.post("/postPlantInfo", urlencodedParser, (req, res) => {
  if (!req.body) return res.sendStatus(400);

  let plantTemp = req.body.plantTemp;
  let plantWet = req.body.plantWet;

  Plants.create({
    temp: plantTemp,
    wet: plantWet,
  })
    .then(() => res.status(200).send("Информация добавилась"))
    .catch((e) => {
      res.status(500).send(e);
    });
});
