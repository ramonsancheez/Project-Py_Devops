import webbrowser
import sys
import os
sys.path.append(".")

# Función que abre directamente la página de HUGO al acabar el código
def abrirHugo():
    # Cambia al directorio especificado
    os.chdir('./frontend/webComida.com')   
    hugoUrl = "http://localhost:1313/"
    # Abre la url en el navegador predefinido
    webbrowser.open_new(hugoUrl)
    # Escribe en la terminal hugo server para que abra HUGO
    os.system("hugo server")