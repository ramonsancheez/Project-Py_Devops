from turtle import up
from pymongo import MongoClient
import certifi
updateDoc = {"titulo":"Pizza Vegana"}
newInfo ={"descriptionMenu":"comida riquisima"}
def updateItem(updateDoc, newInfo):
    try:
        cluster = MongoClient('mongodb+srv://m001-student:mongo123@cluster0.qmgmx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority', tlsCAFile=certifi.where())
        baseDatos = cluster.proyecto
        coleccion = baseDatos.menus_with_schema
        respuesta = input("Va a actualizar un ítem, asegúrese de que es el correcto. ¿Desea actualizarlo? (S/N):  ")
        
        lowRespuesta = respuesta.lower()
        if lowRespuesta == "s":
            coleccion.update_one(updateDoc,{"$set":newInfo}) 
        else:
            raise ValueError
    except:
        print("El item no se pudo actualizar")
        exit()
    else:
        print("Se actualizó correctamente")
        exit()

updateItem(updateDoc,newInfo) 