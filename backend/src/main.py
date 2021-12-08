from accesoDatos.conexionBasedatos import connectionBBDD
from logica.convertirMarkdown.convertirMarkdown import creadorMarkdown
from logica.conectarHugo.conectarHugo import conectarHugo 
from os import system
system('cls')

def principal():
    
    baseDatos = connectionBBDD()
    creadorMarkdown(baseDatos, "ComidaChatarra")
    creadorMarkdown(baseDatos, "ComidaVeganaIntergalactica")
    creadorMarkdown(baseDatos, "ComidaBabyYoda")
    conectarHugo()

principal()
