import webbrowser
import sys
import os
sys.path.append(".")

def abrirHugo(hugoUrl):
    try:
        os.chdir('./frontend/webComida.com')
        webbrowser.open_new(hugoUrl)
        os.system("hugo server")
    except:
        return False
    else:
        return True