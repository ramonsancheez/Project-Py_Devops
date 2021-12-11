from backend.test.pruebas.stateObject import stateCaracteristicas
import pytest

@pytest.mark.stateCaracteristicas
def test_correctObject():
    documento = {"titulo":"carneSabrosa", "state":{"energy":34, "toxity":56, "oxygen": 34}}
    diccionarioState = documento["state"]
    diccionario = stateCaracteristicas(diccionarioState)
    assert diccionario == True

@pytest.mark.stateCaracteristicas
def test_lenIncorrect():
    documento = {"titulo":"carneSabrosa", "state":{"Carne de jupiter":34, "fuego de marte":21}}
    diccionarioState = documento["state"]
    diccionario = stateCaracteristicas(diccionarioState)
    assert diccionario == False

@pytest.mark.stateCaracteristicas
def test_typeIncorrect():
    documento = {"titulo":"carneSabrosa", "state":34}
    diccionarioState = documento["state"]
    diccionario = stateCaracteristicas(diccionarioState)
    assert diccionario == False

