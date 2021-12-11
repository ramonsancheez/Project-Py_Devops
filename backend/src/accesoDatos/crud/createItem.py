from pymongo import MongoClient
import certifi

def createItem():
    cluster = MongoClient('mongodb+srv://m001-student:mongo123@cluster0.qmgmx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority', tlsCAFile=certifi.where())
    baseDatos = cluster.proyecto
    coleccion = baseDatos.menus_with_schema

    newItem = { "name": "John", "address": "Highway 37", "age":37 }
    respuesta = input(f"Va a añadir {newItem} a la base de datos, si desea cambiar los datos, hágalo en el editor de texto. ¿Desea añadir ese ítem? (S/N): ")
    respuesta.lower()
    if respuesta == "s":
        coleccion.insert_one(newItem)
    else:
        print("No se añadió nada a la colección")
        exit()
createItem()