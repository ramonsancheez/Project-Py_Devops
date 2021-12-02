from pymongo import MongoClient
import certifi

def connectionBBDD():
    try:
        cluster = MongoClient('mongodb+srv://m01-student:mongo123@cluster0.qmgmx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority', tlsCAFile=certifi.where())
        baseDatos = cluster.proyecto
        len(baseDatos)
    except:
        print("No puedo realizarse la conexión con la base de datos, los archivos no han sido creados y la carpeta de hugo esta desabitada")
        exit()
    else:
        print("Se realizó la conexión correctamente")
        return baseDatos