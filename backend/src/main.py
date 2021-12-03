from accesoDatos.conexionBasedatos import connectionBBDD
from logica.convertirMarkdown.convertirMarkdown import markdown
from os import system
system('cls')

def principal():
    
    baseDatos = connectionBBDD()
    markdown(baseDatos, "Comida Chatarra")
    markdown(baseDatos, "Comida Vegana Intergaláctica")
    markdown(baseDatos, "Comida Baby Yoda")


principal()
