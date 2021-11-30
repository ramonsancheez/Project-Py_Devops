from src.accesoDatos.conexionBasedatos import connectionBBDD
import pytest

@pytest.mark.connectionBBDD
def isInsideDB():
    assert isInsideDB("Title") == False