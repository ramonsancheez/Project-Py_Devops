<<<<<<< HEAD
from src.main import isInsideDB
<<<<<<< HEAD
from pytest

@pytest.mark.isInsideDB
def test_isInsideTitle:
    assert 
=======
=======
from src.accesoDatos.conexionBasedatos import connectionBBDD
>>>>>>> Ramon-features
import pytest

@pytest.mark.connectionBBDD
def isInsideDB():
    assert isInsideDB("Title") == False
>>>>>>> origin/Ramon-features
