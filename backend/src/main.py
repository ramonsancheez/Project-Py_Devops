from pymongo import MongoClient
import certifi
from pprint import pprint
# URL de la base de datos

def isInsideDB():
    
    cluster = MongoClient('mongodb+srv://m001-student:mongo123@cluster0.qmgmx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority', tlsCAFile=certifi.where())

    items = cluster.proyecto.menus.find()

    lista = []

    for i in items:
        lista.append(i)
    pprint(lista)

    for j in range(len(lista)):
        print(lista[j]["stock"])