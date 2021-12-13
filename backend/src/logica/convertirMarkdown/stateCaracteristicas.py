
# Función que pasa el diccionario de state a un único string
def stateCaracteristicas(documento):
    try:
        caracteristicasEspeciales = "**Las características especiales del menú son:** \n"
        diccionarioState = documento['state']
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
        print("Compruebe mejor su pedido, algo ha aido mal")
        exit()
    else:
        return caracteristicasEspeciales
