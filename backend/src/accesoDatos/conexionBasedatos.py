from pymongo import MongoClient
import certifi

def connectionBBDD():
    try:
        cluster = MongoClient('mongodb+srv://m001-student:mongo123@cluster0.qmgmx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority', tlsCAFile=certifi.where())
        baseDatos = cluster.proyecto
        "menus_with_schema" in baseDatos.list_collection_names()
    except:
        print("No pudo realizarse la conexion con la base de datos")
        exit()
    else:
        print("La conexión con la base de datos se realizó correctamente")
        return baseDatos