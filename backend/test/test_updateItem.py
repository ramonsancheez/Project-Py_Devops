from backend.test.pruebas.updateItem import updateItem
from pymongo import MongoClient
import pytest
import certifi

@pytest.mark.updateItem
def test_correctoUpdate():
    cluster = MongoClient('mongodb+srv://m001-student:mongo123@cluster0.qmgmx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority', tlsCAFile=certifi.where())
    baseDatos = cluster.proyecto
    coleccion = baseDatos.menus
    respuesta = "s"
    updatedItem = {"titulo":"Pizza Vegana"}
    comprobacion = updateItem(coleccion, respuesta, updatedItem)
    assert comprobacion == True

@pytest.mark.updateItem
def test_incorrectaUrl():
    cluster = MongoClient('mongodb+srv://-student:mongo123@cluster0.qmgmx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority', tlsCAFile=certifi.where())
    baseDatos = cluster.proyecto
    coleccion = baseDatos.menus
    respuesta = "s"
    updatedItem = {"name":"Pizza Vegana"}
    comprobacion = updateItem(coleccion, respuesta, updatedItem)
    assert comprobacion == False

@pytest.mark.updateItem
def test_incorrectaRespuesta():
    cluster = MongoClient('mongodb+srv://m001-student:mongo123@cluster0.qmgmx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority', tlsCAFile=certifi.where())
    baseDatos = cluster.proyecto
    coleccion = baseDatos.menus
    respuesta = "n"
    updatedItem = {"name":"Pizza Vegana"}
    comprobacion = updateItem(coleccion, respuesta, updatedItem)
    assert comprobacion == False
