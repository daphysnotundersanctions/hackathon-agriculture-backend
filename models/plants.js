import { DataTypes } from "sequelize";
import { db } from "../db.js";

export const Plants = db.define("Plants", {
  requestId: {
    type: DataTypes.INTEGER,
    unique: true,
  },
  temp: {
    type: DataTypes.INTEGER,
  },
  wet: {
    type: DataTypes.INTEGER,
  },
});
