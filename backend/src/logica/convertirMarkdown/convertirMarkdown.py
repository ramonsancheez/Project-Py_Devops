from convertirMarkdown.ingredientsList import ingredientsList

def bucle(diccionario):
    f = open("./archivosMarkdown/" + diccionario["titulo"] + ".md", "w", encoding="utf-8")
    for key in diccionario:
        string = ""
        valor = diccionario[key]
        if key == "_id": 
            continue
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
            f.write(lista + "\n" + "\n")
            continue
        if key == "stock":
            string += "Stock disponible: " + str(valor) + " unidades"
        f.write(string + "\n" + "\n")
    f.close()

def markdown(diccionarioDiccionario):
    i = 0
    while i < len(diccionarioDiccionario):
        bucle(diccionarioDiccionario[i])
        i += 1
        if i == len(diccionarioDiccionario)-1:
            return diccionarioDiccionario[i]