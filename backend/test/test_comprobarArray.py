from backend.test.pruebas.ingredientsArray import ingredientsArray
import pytest

@pytest.mark.ingredientsArray
def test_unionArray():
    documento = {"titulo":"carneSabrosa", "ingredients":["Carne de jupiter", "Urano de pluton", "fuego de marte"]}
    string = ingredientsArray(documento)
    assert string == True

@pytest.mark.ingredientsArray
def test_emptyArray():
    documento = {"ingredients":[]}
    string = ingredientsArray(documento)
    assert string == False 