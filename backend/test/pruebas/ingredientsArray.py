def ingredientsArray(documento):
    try:
        valor = documento['ingredients']
        ingredientesLista = "**Los ingredientes que lleva el menú son:** "

        for ingrediente in valor:
                lowerIngredient = ingrediente.lower()
                if ingrediente == valor[-1]:
                    ingredientesLista += lowerIngredient + "."
                else:
                    ingredientesLista += lowerIngredient + ", "

        if ingredientesLista.count(",") != 2 and ingredientesLista.count(".") != 1:
            raise ValueError
    except:
        return False
    else:    
        return True