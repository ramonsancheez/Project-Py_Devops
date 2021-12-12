from pymongo import MongoClient
import certifi

def deleteItem():
    try:
        cluster = MongoClient('mongodb+srv://m001-student:mongo123@cluster0.qmgmx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority', tlsCAFile=certifi.where())
        baseDatos = cluster.proyecto
        coleccion = baseDatos.menus_with_schema

        deletedItem = { "name": "John", "address": "Highway 37" }
        respuesta = input(f"Va a eliminar {deletedItem} de la base de datos, si desea cambiar los datos, hágalo en el editor de texto. ¿Desea eliminar ese ítem? (S/N): ")
        respuesta.lower()
        if respuesta == "s":
            coleccion.delete_one(deletedItem)
        else:
            raise ValueError
    except:
        print("No se puedo eliminar el item")
        exit()
    else:
        print("Se eliminó el item de la colección")
        return True

    # coleccion.delete_many({"name": "John"}) #Elimina todos los items que tengan key NAME y valor Mr.GenericTraceback
    # coleccion.remove() Elimina todos los ítems
    # coleccion.delete_one(deletedItem) Elimina ese item

deleteItem()