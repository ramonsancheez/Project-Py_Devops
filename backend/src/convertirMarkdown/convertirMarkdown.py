import sys
sys.path.append(".")
from backend.src.accesoDatos.conexionBasedatos import lista

def titulo(d):
    numHastags = 2
    hastags = "#" * numHastags
    titulo = d["titulo"]
    f = open(titulo + ".md", "w")
    f.write(hastags + " " + titulo + "\n")
    f.close()

def descriptionMenu(d):
    descriptionMenu = d["descriptionMenu"]
    f = open(d["titulo"] + ".md", "a")
    f.write(descriptionMenu + " " + "\n")
    f.close()

def stock(d):
    stock = d["stock"]
    f = open(d["titulo"] + ".md", "a")
    f.write(stock + " " + "\n")
    f.close()

def precio(d):
    precio = d["precio"]
    f = open(d["titulo"] + ".md", "a")
    f.write(precio + " " + "\n")
    f.close()

def ingredientes(d):
    ingredientes = d["ingredientes"]
    f = open(d["titulo"] + ".md", "a")
    f.write(ingredientes + " " + "\n")
    f.close()

def category(d):
    category = d["category"]
    f = open(d["titulo"] + ".md", "a")
    f.write(category + " " + "\n")
    f.close()

def state(d):
    state = d["state"]
    f = open(d["titulo"] + ".md", "a")
    f.write(state + " " + "\n")
    f.close()

def markdown(listaDiccionario):
    i = 0
    while i < len(listaDiccionario):
        titulo(listaDiccionario[i])
        descriptionMenu(listaDiccionario[i])
        stock(listaDiccionario[i])
        precio(listaDiccionario[i])
        ingredientes(listaDiccionario[i])
        category(listaDiccionario[i])
        state(listaDiccionario[i])
        i += 1

markdown(lista)