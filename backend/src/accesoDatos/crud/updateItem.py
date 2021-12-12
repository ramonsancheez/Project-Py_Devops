from pymongo import MongoClient
import certifi

def updateItem():
    try:
        cluster = MongoClient('mongodb+srv://m001-student:mongo123@cluster0.qmgmx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority', tlsCAFile=certifi.where())
        baseDatos = cluster.proyecto
        coleccion = baseDatos.menus_with_schema
        respuesta = input("Va a actualizar un ítem, asegúrese de que es el correcto. ¿Desea actualizarlo? (S/N):  ")
        
        lowRespuesta = respuesta.lower()
        if lowRespuesta == "s":
            coleccion.update_one({"titulo":"Pizza Vegana"},{"$set":{"descriptionMenu":"comida riquisima"}})
        else:
            raise ValueError
    except:
        print("El item no se pudo actualizar")
        exit()
    else:
        print("Se actualizó correctamente")
        exit()

updateItem() 