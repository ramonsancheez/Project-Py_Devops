import os 
import shutil

# Función que transfiere los archivos de la carpeta archivosMarkdown a la carpeta posts de HUGO
def transferirMarkdown():
    
    try:
        # Obtenemos la ruta de origen
        rutaOrigen = f'{os.getcwd()}/archivosMarkdown/'
        # Obtenemos una lista con los archivos que hay en la ruta de origen
        archivosLista = os.listdir(rutaOrigen)
        if len(archivosLista) == 0:
            raise ValueError
    except:
        print("La carpeta archivosMarkdown está vacía, por lo que no se le puede transferir ningún archivo a HUGO")
        exit()
    else:
        contenido = "Esta es una lista del contenido que hay en la carpeta archivosMarkdown: \n" +  str(archivosLista)
        # Obtenemos la ruta a la que tienen que llegar los archivos
        rutaDestino =f'{os.getcwd()}/frontend/webComida.com/content/posts'
        # Recorremos la lista creada anteriormente
        for archivo in archivosLista:
            # Copiamos archivo en la ruta de destino
            shutil.copy(os.path.join(rutaOrigen, archivo), rutaDestino)
        print(contenido)
        return transferirMarkdown