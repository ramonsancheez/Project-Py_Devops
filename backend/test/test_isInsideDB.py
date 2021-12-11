from backend.test.pruebas.completedConnection import connectionBBDD
import pytest

@pytest.mark.connectionBBDD
def test_BBDD_url_correcta():
    url = "mongodb+srv://m001-student:mongo123@cluster0.qmgmx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    baseDatos = connectionBBDD(url)
    assert baseDatos == True
    
@pytest.mark.connectionBBDD
def test_BBDD_url_incorrecta():
    url = "urlErronea"
    baseDatos = connectionBBDD(url)
    assert baseDatos == False   