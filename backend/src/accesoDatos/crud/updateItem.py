from pymongo import MongoClient
import certifi

def updateItem():
    cluster = MongoClient('mongodb+srv://m001-student:mongo123@cluster0.qmgmx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority', tlsCAFile=certifi.where())
    baseDatos = cluster.proyecto
    coleccion = baseDatos.menus_with_schema

    respuesta = input("Va a actualizar un ítem, asegúrese de que es el correcto. ¿Desea actualizarlo? (S/N):  ")
    if respuesta.lower() == "s":
        coleccion.update_one({"name":"John"},{"$set":{"adress":"Plaza Mayor"}})
    else:
        print("No se actualizó ningún ítem")
        exit()  
updateItem()