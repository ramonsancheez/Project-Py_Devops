from accesoDatos.conexionBasedatos import connectionBBDD
from convertirMarkdown.convertirMarkdown import markdown

def principal():
    
    lista = connectionBBDD()
    markdown(lista)

principal()