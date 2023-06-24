import { Sequelize } from "sequelize";

export const db = new Sequelize("api", "postgres", "root", {
  HOST: "localhost",
  operatorsAliases: 0,
  dialect: "postgres",
  pool: {
    max: 5,
    min: 0,
    acquire: 30000,
    idle: 10000,
  },
});

try {
  await db.authenticate();
  console.log("Connection has been established successfully.");
} catch (error) {
  console.error("Unable to connect to the database:", error);
}
