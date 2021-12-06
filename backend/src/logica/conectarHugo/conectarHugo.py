import os 
import shutil

def conectarHugo():
    try:
        rutaOrigen = f'{os.getcwd()}/archivosMarkdown/'
        archivosLista = os.listdir(rutaOrigen)
        assert archivosLista

    except:
        print("La carpeta archivosMarkdown está vacía, por lo que no se le puede transferir ningún archivo a HUGO")
        exit()
    else:
        contenido = "Esta es una lista del contenido que hay en la carpeta archivosMarkdown: \n" +  str(archivosLista)
        rutaOrigen = f'{os.getcwd()}/archivosMarkdown/'
        rutaDestino =f'{os.getcwd()}/frontend/webProyecto/content/'
        for archivo in archivosLista:
            shutil.copy(os.path.join(rutaOrigen, archivo), rutaDestino)
        print(contenido)
        return conectarHugo