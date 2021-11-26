from pymongo import MongoClient
from pprint import pprint

cluster = MongoClient("mongodb+srv://m001-student:mongo123@cluster0.qmgmx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster.proyecto
documentos = db.menus.find()
# Pprint se utiliza para visualizar los datos de forma esquemática
for i in documentos:    
    pprint(i)
