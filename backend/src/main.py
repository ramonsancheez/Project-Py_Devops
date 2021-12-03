from accesoDatos.conexionBasedatos import connectionBBDD
from logica.convertirMarkdown.convertirMarkdown import creadorMarkdown
from os import system
system('cls')

def principal():
    
    baseDatos = connectionBBDD()
    creadorMarkdown(baseDatos, "Comida Chatarra")
    creadorMarkdown(baseDatos, "Comida Vegana Intergaláctica")
    creadorMarkdown(baseDatos, "Comida Baby Yoda")

principal()
