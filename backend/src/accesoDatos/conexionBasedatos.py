from pymongo import MongoClient
import certifi

# Función que obtiene la baseDatos y comprueba si en esa base de datos existe una colacción con nombre "menus_with_schema"
def connectionBBDD(bbddUrl):
    
    try:
        cluster = MongoClient(bbddUrl, tlsCAFile=certifi.where())
        baseDatos = cluster.proyecto
        # Comprueba que en esa baseDatos existe esa coleccion
        "menus_with_schema" in baseDatos.list_collection_names() 
    # Si no existe, acaba la función
    except: 
        print("No pudo realizarse la conexion con la base de datos \n")
        exit()
    # Si existe, devuelve esa baseDatos
    else:
        print("La conexión con la base de datos se realizó correctamente \n")
        return baseDatos