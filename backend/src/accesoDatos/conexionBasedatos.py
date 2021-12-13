from pymongo import MongoClient
import certifi

def connectionBBDD(bbddUrl):
    try:
        cluster = MongoClient(bbddUrl, tlsCAFile=certifi.where())
        baseDatos = cluster.proyecto
        "menus_with_schema" in baseDatos.list_collection_names()
    except:
        print("No pudo realizarse la conexion con la base de datos \n")
        exit()
    else:
        print("La conexión con la base de datos se realizó correctamente \n")
        return baseDatos
