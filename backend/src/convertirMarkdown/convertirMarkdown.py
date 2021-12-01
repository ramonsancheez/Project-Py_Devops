def bucle(diccionario):
    f = open("./archivosMarkdown/" + diccionario["titulo"] + ".md", "w", encoding="utf-8")
    for key in diccionario:
        valor = diccionario[key]
        if key == "_id": 
            continue
        
        # if key == "titulo": 
        #     f.write("# ")
        # if key == "price": 
        #     f.write("El precio es: ")
        # if key == "category":
        #     f.write("Categoria: **")
        # if key == "stock":
        #     f.write("Sólo quedan: ")
        f.write(str(valor))
        # if key == "stock":
        #     f.write(" unidades")
        # if key == "category":
        #     f.write("**")
        # if key == "price": 
        #     f.write("€")
        # f.write("\n" + "\n")
    f.close()

def markdown(diccionarioDiccionario):
    i = 0
    while i < len(diccionarioDiccionario):
        bucle(diccionarioDiccionario[i])
        i += 1