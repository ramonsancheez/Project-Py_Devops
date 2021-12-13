import os 
import shutil

def transferirMarkdown():
    try:
        rutaOrigen = f'{os.getcwd()}/archivosMarkdown/'
        archivosLista = os.listdir(rutaOrigen)
        if len(archivosLista) == 0:
            raise ValueError
    except:
        print("La carpeta archivosMarkdown está vacía, por lo que no se le puede transferir ningún archivo a HUGO")
        exit()
    else:
        contenido = "Esta es una lista del contenido que hay en la carpeta archivosMarkdown: \n" +  str(archivosLista)
        rutaDestino =f'{os.getcwd()}/frontend/webComida.com/content/'
        for archivo in archivosLista:
            shutil.copy(os.path.join(rutaOrigen, archivo), rutaDestino)
        print(contenido)