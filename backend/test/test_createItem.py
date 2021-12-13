from backend.test.pruebas.createItem import createItem
from pymongo import MongoClient
import pytest
import certifi

@pytest.mark.createItem
def test_correctItem():
    cluster = MongoClient('mongodb+srv://m001-student:mongo123@cluster0.qmgmx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority', tlsCAFile=certifi.where())
    baseDatos = cluster.proyecto
    coleccion = baseDatos.menus_with_schema
    respuesta = "s"
    newItem = { "titulo": "John", "stock":37, "price":3.99, "descriptionMenu": "Highway 37", "ingredients":["hola","soy", "ramon"], "category":"ComidaChatarra", "state":{"energy":34, "radiation":23, "toxicity":34} }
    comprobacion = createItem(coleccion, newItem, respuesta)
    assert comprobacion == True


@pytest.mark.createItem
def test_incorrectItem():
    cluster = MongoClient('mongodb+srv://m001-student:mongo123@cluster0.qmgmx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority', tlsCAFile=certifi.where())
    baseDatos = cluster.proyecto
    coleccion = baseDatos.menus_with_schema
    respuesta = "S"
    newItem = newItem = { "title": "John", "stock":37, "descriptionMenu": "Highway 37", "ingredients":["hola","soy", "ramon"], "category":"ComidaChatarra", "state":{"energy":34, "radiation":23, "toxicity":34} }
    comprobacion = createItem(coleccion, newItem, respuesta)
    assert comprobacion == False

@pytest.mark.createItem
def test_incorrectUrl():
    cluster = MongoClient('mongodb+srv://student:mongo123@cluster0.qmgmx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority', tlsCAFile=certifi.where())
    baseDatos = cluster.proyecto
    coleccion = baseDatos.menus_with_schema
    respuesta ="S"
    newItem = newItem = { "titulo": "John", "stock":37, "price":3.99, "descriptionMenu": "Highway 37", "ingredients":["hola","soy", "ramon"], "category":"ComidaChatarra", "state":{"energy":34, "radiation":23, "toxicity":34} }
    comprobacion = createItem(coleccion, newItem, respuesta)
    assert comprobacion == False

@pytest.mark.createItem
def test_incorrectRespuesta():
    cluster = MongoClient('mongodb+srv://student:mongo123@cluster0.qmgmx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority', tlsCAFile=certifi.where())
    baseDatos = cluster.proyecto
    coleccion = baseDatos.menus_with_schema
    respuesta ="N"
    newItem = newItem = { "titulo": "John", "stock":37, "price":3.99, "descriptionMenu": "Highway 37", "ingredients":["hola","soy", "ramon"], "category":"ComidaChatarra", "state":{"energy":34, "radiation":23, "toxicity":34} }
    comprobacion = createItem(coleccion, newItem, respuesta)
    assert comprobacion == False
