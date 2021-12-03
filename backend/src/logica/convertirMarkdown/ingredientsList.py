def ingredientsList(diccionario):
    valor = diccionario['ingredients']
    ingredientesLista = "**Los ingredientes que lleva el menú son:** "
    for ingrediente in valor:
            lowerIngredient = ingrediente.lower()
            if ingrediente == valor[-1]:
                ingredientesLista += lowerIngredient + "."
            else:
                ingredientesLista += lowerIngredient + ", "
    return ingredientesLista
            