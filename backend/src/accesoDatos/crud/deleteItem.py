from pymongo import MongoClient
import certifi

def deleteItem():
    cluster = MongoClient('mongodb+srv://m001-student:mongo123@cluster0.qmgmx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority', tlsCAFile=certifi.where())
    baseDatos = cluster.proyecto
    coleccion = baseDatos.pruebaCollectionEmpty
    deletedItem = { "name": "John", "address": "Highway 37" }

    respuesta = input(f"Va a eliminar {deletedItem} de la base de datos, si desea cambiar los datos, hágalo en el editor de texto. ¿Desea eliminar ese ítem? (S/N): ")
    respuesta.lower()
    if respuesta == "s":
        coleccion.insert_one(deletedItem)
    else:
        print("No se eliminó nada de la colección")
        exit()
    # coleccion.delete_many({"name": "John"}) #Elimina todos los items que tengan key NAME y valor Mr.GenericTraceback
    # # coleccion.remove() Elimina todos los ítems
    # # coleccion.delete_one(deletedItem) Elimina ese item

deleteItem()