from accesoDatos.conexionBasedatos import connectionBBDD
from logica.convertirMarkdown.convertirMarkdown import creadorMarkdown
from logica.transferirMarkdown.conectarHugo import transferirMarkdown 
from logica.abrirHugo.abrirHugo import abrirHugo
from os import system
system("cls")


def principal():
    
    bbddUrl = "mongodb+srv://m001-student:mongo123@cluster0.qmgmx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

    baseDatos = connectionBBDD(bbddUrl)
    creadorMarkdown(baseDatos, "ComidaChatarra")
    creadorMarkdown(baseDatos, "ComidaVeganaIntergalactica")
    creadorMarkdown(baseDatos, "ComidaBabyYoda")    
    transferirMarkdown()
    abrirHugo()

principal()