from src.main import isInsideDB
<<<<<<< HEAD
from pytest

@pytest.mark.isInsideDB
def test_isInsideTitle:
    assert 
=======
import pytest

@pytest.mark.isInsideDB
def isInsideDB():
    assert isInsideDB("Title") == False
>>>>>>> origin/Ramon-features
