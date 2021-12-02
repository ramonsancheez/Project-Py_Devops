def ingredientsList(diccionario):
    ingredientesLista = "**Los ingredientes que conlleva el menú son:** "
    for key in diccionario:
        valor = diccionario[key]
        if key == "ingredients":
            ingredientesLista = "**Los ingredientes que lleva el menú son:** "
            for ingrediente in valor:
                    lowerIngredient = ingrediente.lower()
                    if ingrediente == valor[-1]:
                        ingredientesLista += lowerIngredient + "."
                    else:
                        ingredientesLista += lowerIngredient + ", "
    return ingredientesLista 
            