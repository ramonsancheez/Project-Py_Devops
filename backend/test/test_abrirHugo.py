from backend.test.pruebas.abrirHugo import abrirHugo
import pytest

@pytest.mark.abrirHugo
def test_URLcorrect():
    hugoUrl = "http://localhost:1313/"
    URLcorrect = abrirHugo(hugoUrl)
    assert URLcorrect == True