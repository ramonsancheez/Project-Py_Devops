<<<<<<< HEAD
from pymongo import MongoClient
from pprint import pprint

cluster = MongoClient("mongodb+srv://m001-student:mongo123@cluster0.qmgmx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster.proyecto
documentos = db.menus.find()
# Pprint se utiliza para visualizar los datos de forma esquemática
for i in documentos:    
    pprint(i)
=======
from accesoDatos.conexionBasedatos import connectionBBDD
from logica.convertirMarkdown.convertirMarkdown import markdown
from os import system
system('cls')

def principal():
    
    baseDatos = connectionBBDD()
    markdown(baseDatos, "Comida Chatarra")
    markdown(baseDatos, "Comida Vegana Intergaláctica")
    markdown(baseDatos, "Comida Baby Yoda")


principal()
>>>>>>> Ramon-features
