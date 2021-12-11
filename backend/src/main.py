from accesoDatos.conexionBasedatos import connectionBBDD
from logica.convertirMarkdown.convertirMarkdown import creadorMarkdown
from logica.conectarHugo.conectarHugo import conectarHugo 
from logica.abrirHugo.abrirHugo import abrirHugo
from os import system
system("cls")


def principal():
    
    url = "mongodb+srv://m001-student:mongo123@cluster0.qmgmx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

    baseDatos = connectionBBDD(url)
    creadorMarkdown(baseDatos, "ComidaChatarra")
    creadorMarkdown(baseDatos, "ComidaVeganaIntergalactica")
    creadorMarkdown(baseDatos, "ComidaBabyYoda")    
    conectarHugo()
    abrirHugo()

principal()