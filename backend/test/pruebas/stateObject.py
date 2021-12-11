def stateCaracteristicas(diccionarioState):
    try:
        caracteristicasEspeciales = "**Las características especiales del menú son:** \n"
        if type(diccionarioState) != dict:
            raise ValueError
        if len(diccionarioState) != 3:
            raise ValueError
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
    except:
        return False
    else:
        return True
