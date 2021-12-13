import webbrowser
import sys
import os
sys.path.append(".")

def abrirHugo():
    os.chdir('./frontend/webComida.com')
    print("estoy en la carpera deseada")    
    hugoUrl = "http://localhost:1313/"
    webbrowser.open_new(hugoUrl)
    os.system("hugo server")

