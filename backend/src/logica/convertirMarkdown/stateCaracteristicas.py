def stateCaracteristicas(diccionario):
    caracteristicasEspeciales = "**Las características especiales del menú son:** \n"
    diccionarioState = diccionario['state']
    valores = diccionarioState.values()
    valoresLista = list(valores)
    keys = diccionarioState.keys()
    for key in keys:
        capKeys = key.capitalize()
        caracteristicasEspeciales += "- " + capKeys + ": "
        for valor in valoresLista:
            caracteristicasEspeciales += str(valor) + "\n"
            valoresLista.remove(valor)
            break
    return caracteristicasEspeciales
