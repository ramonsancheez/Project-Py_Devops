db.createCollection("menus", {
    validator: {
      $jsonSchema: {
        bsonType: "object",
        required: [
          "titulo",
          "stock",
          "price",
          "descriptionMenu",
          "ingredients",
          "category",
          "state",
        ],
        properties: {
          titulo: {
            bsonType: "string",
            description: "must be a string with name of menu",
          },
          stock: {
            bsonType: "int",
            description: "must be an integer with stock of one menu",
          },
          price: {
            bsonType: "double",
            description: "must be a double with the price of menu",
          },
          descriptionMenu: {
            bsonType: "string",
            description: "must be a string with description of menu",
          },
          ingredients: {
            bsonType: "array",
            description: "must be an array with ingredients of menus",
            items: {
              bsonType: "string",
              description: "must be a string with ingredient of menu",
            },
          },
          category: {
            bsonType: "string",
            description: "must be a string with category of menu",
            enum: ["Comida Vegana Intergaláctica", "Comida Baby Yoda", "Comida Chatarra"]
          },
          state: {
            bsonType: "object",
            description: "must be an object with a series of number properties",
            properties: {
              energy: { bsonType: "int" },
              radiation: { bsonType: "int" },
              toxicity: { bsonType: "int" },
            },
          },
        },
      },
    },
  });
  