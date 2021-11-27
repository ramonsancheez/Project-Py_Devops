from src.main import isInsideDB
import pytest

@pytest.mark.isInsideDB
def isInsideDB():
    assert isInsideDB("Title") == False