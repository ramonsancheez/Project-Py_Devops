from accesoDatos.conexionBasedatos import connectionBBDD
from logica.convertirMarkdown.convertirMarkdown import markdown

def principal():
    
    lista = connectionBBDD()
    markdown(lista)

principal()