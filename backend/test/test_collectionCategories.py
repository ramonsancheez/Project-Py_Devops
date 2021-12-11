from backend.test.pruebas.collectionCategory import selector_Datos
from pymongo import MongoClient
import certifi
import pytest

@pytest.mark.selector_Datos
def test_collectionFull():
    cluster = MongoClient("mongodb+srv://m001-student:mongo123@cluster0.qmgmx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", tlsCAFile=certifi.where())
    baseDatos = cluster.proyecto
    coleccion = baseDatos.menus_with_schema
    categoria = "ComidaChatarra"
    collectionFull = selector_Datos(coleccion, categoria)
    assert collectionFull == True

@pytest.mark.selector_Datos
def test_collectionEmpty():
    cluster = MongoClient("mongodb+srv://m001-student:mongo123@cluster0.qmgmx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", tlsCAFile=certifi.where())
    baseDatos = cluster.proyecto
    coleccion = baseDatos.collectionEmpty
    categoria = "ComidaChatarra"
    collectionFull = selector_Datos(coleccion, categoria)
    assert collectionFull == False

@pytest.mark.selector_Datos
def test_categoriaInexistente():
    cluster = MongoClient("mongodb+srv://m001-student:mongo123@cluster0.qmgmx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", tlsCAFile=certifi.where())
    baseDatos = cluster.proyecto
    coleccion = baseDatos.menus_with_schema
    categoria = "Comida"
    collectionEmpty = selector_Datos(coleccion, categoria)
    assert collectionEmpty == False

@pytest.mark.selector_Datos
def test_categoriaInexiste_collectionEmpty():
    cluster = MongoClient("mongodb+srv://m001-student:mongo123@cluster0.qmgmx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", tlsCAFile=certifi.where())
    baseDatos = cluster.proyecto
    coleccion = baseDatos.collectionEmpty
    categoria = "Comida"
    collectionEmpty = selector_Datos(coleccion, categoria)
    assert collectionEmpty == False