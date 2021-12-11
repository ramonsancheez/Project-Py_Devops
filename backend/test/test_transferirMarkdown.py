from backend.test.pruebas.trasfMarkdown import transferirMarkdown
import pytest
import os

@pytest.mark.transferirMarkdown
def test_rutaCorrecta():
    rutaOrigen = f'{os.getcwd()}/archivosMarkdown/'
    archivosLista = os.listdir(rutaOrigen)
    ruta = transferirMarkdown(rutaOrigen, archivosLista)
    assert ruta == True

@pytest.mark.transferirMarkdown
def test_sinArchivosMD():
    rutaOrigen = f'{os.getcwd()}/archivosMarkdown/'
    archivosLista = []
    ruta = transferirMarkdown(rutaOrigen, archivosLista)
    assert ruta == False

