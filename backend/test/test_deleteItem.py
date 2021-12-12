from backend.test.pruebas.deleteItem import deleteItem
from pymongo import MongoClient
import pytest
import certifi

@pytest.mark.deleteItem
def test_correctEliminado():
    cluster = MongoClient('mongodb+srv://m001-student:mongo123@cluster0.qmgmx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority', tlsCAFile=certifi.where())
    baseDatos = cluster.proyecto
    coleccion = baseDatos.menus_with_schema
    deletedItem = { "title": "John", "address": "Highway 37" }
    respuesta = "S"
    comprobacion = deleteItem(coleccion, deletedItem, respuesta)
    assert comprobacion == True

@pytest.mark.deleteItem
def test_incorrectItem():
    cluster = MongoClient('mongodb+srv://m001-student:mongo123@cluster0.qmgmx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority', tlsCAFile=certifi.where())
    baseDatos = cluster.proyecto
    coleccion = baseDatos.menus_with_schema
    deletedItem = { "name": "John", "address": "Highway 37" }
    respuesta = "S"
    comprobacion = deleteItem(coleccion, deletedItem, respuesta)
    assert comprobacion == False

@pytest.mark.deleteItem
def test_incorrectUrl():
    cluster = MongoClient('mongodb+srv://student:mongo123@cluster0.qmgmx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority', tlsCAFile=certifi.where())
    baseDatos = cluster.proyecto
    coleccion = baseDatos.menus_with_schema
    deletedItem = { "name": "John", "address": "Highway 37" }
    respuesta = "S"
    comprobacion = deleteItem(coleccion, deletedItem, respuesta)
    assert comprobacion == False

@pytest.mark.deleteItem
def test_incorrectRespuesta():
    cluster = MongoClient('mongodb+srv://m001-student:mongo123@cluster0.qmgmx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority', tlsCAFile=certifi.where())
    baseDatos = cluster.proyecto
    coleccion = baseDatos.menus_with_schema
    deletedItem = { "name": "John", "address": "Highway 37" }
    respuesta = "N"
    comprobacion = deleteItem(coleccion, deletedItem, respuesta)
    assert comprobacion == False