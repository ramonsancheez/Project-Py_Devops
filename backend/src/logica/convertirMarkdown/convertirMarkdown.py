from accesoDatos.listaDiccionarios import selector_Datos
from .ingredientsList import ingredientsList

def escritorMarkdown(diccionario, archivo):
    for key in diccionario:
        string = ""
        valor = diccionario[key]
        if key == "titulo": 
            string += "# " + str(valor)
        if key == "descriptionMenu":
            string += str(valor)
        if key == "price": 
            string += "El precio es de: " + "**" + str(valor) + "€**"
        if key == "category":
            string += "La categoria es: " + "**" + str(valor) + "**"
        if key == "ingredients":
            lista = ingredientsList(diccionario)
            archivo.write(lista + "\n" + "\n")
            continue
        if key == "stock":
            string += "Stock disponible: " + str(valor) + " unidades"
        archivo.write(string + "\n" + "\n")

def creadorMarkdown(baseDatos, categoria):
    listaDiccionarios = selector_Datos(baseDatos, categoria)
    i = 0
    file = open("./archivosMarkdown/" + categoria + ".md", "w", encoding="utf-8")
    while i < len(listaDiccionarios):
        escritorMarkdown(listaDiccionarios[i], file)
        i += 1
    file.close()