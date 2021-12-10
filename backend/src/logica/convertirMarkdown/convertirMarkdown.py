from accesoDatos.listaDiccionarios import selector_Datos
from .ingredientsList import ingredientsList
from .stateCaracteristicas import stateCaracteristicas  
import os


def escritorMarkdown(documento, archivo):
    for key in documento:
        string = ""
        valor = documento[key]
        match key:
            case "_id":
                continue
            case "titulo":
                string += "# " + str(valor)
            case "descriptionMenu":
                string += str(valor)
            case "stock":
                string += "Stock disponible: " + str(valor) + " unidades"
            case "price":
                 string += "El precio es de: " + "**" + str(valor) + "€**"
            case "ingredients":
                string = ingredientsList(documento)
            case "state":
                string = stateCaracteristicas(documento)
            case "category":        
                string += "La categoria es: " + "**" + str(valor) + "**"
        archivo.write(string + "\n" + "\n")



        
def creadorMarkdown(baseDatos, categoria):
    os.makedirs("./archivosMarkdown", exist_ok=True)
    listaDiccionarios = selector_Datos(baseDatos, categoria)
    i = 0
    file = open("./archivosMarkdown/" + categoria + ".md", "w", encoding="utf-8")
    while i < len(listaDiccionarios):
        escritorMarkdown(listaDiccionarios[i], file)
        i += 1
    file.close()