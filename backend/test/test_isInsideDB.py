from backend.src.accesoDatos.conexionBasedatos import connectionBBDD
import pytest

@pytest.mark.connectionBBDD
def test_BBDD_no_vacia():
    baseDatos = connectionBBDD()
    assert baseDatos != None
    