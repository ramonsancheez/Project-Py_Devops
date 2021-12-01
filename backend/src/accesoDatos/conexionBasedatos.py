from pymongo import MongoClient
import certifi

def connectionBBDD():
    try:
    # URL de la base de datos
        cluster = MongoClient('mongodb+srv://m001-student:mongo123@cluster0.qmgmx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority', tlsCAFile=certifi.where())
        items = cluster.proyecto.menus_with_schema.find()
        lista = []
        for i in items:
            lista.append(i)
    except:
        print("No se puede realizar la conexión con la base de datos")
    else:
        print("La conexión con la base de datos fue un éxito")
    finally:
        return lista