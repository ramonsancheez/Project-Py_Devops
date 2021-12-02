from pymongo import MongoClient, errors
import certifi
from pprint import pprint

#def connection(user='m001-student', password='m001-mongodb-basics'):
    
try:
# URL de la base de datos
    cluster = MongoClient('mongodb+srv://m001-student:mongo123@cluster0.qmgmx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority', tlsCAFile=certifi.where())
    items = cluster.proyecto.menus.find()
    lista = []
    for i in items:
        lista.append(i)
except errors.OperationFailure:
    print("No se puede realizar la conexión con la base de datos")
else:
    print("La conexión con la base de datos fue un éxito")
    assert isinstance(lista, list)
    pprint(lista)
if __name__ == '__main__':
    print('a')