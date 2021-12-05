def stateCaracteristicas(diccionario):
    caracteristicasEspeciales = "**Las características especiales del menú son:** \n"
    valor = diccionario['state']
    for caracteristica in valor:
        if caracteristica == valor[0]:
            caracteristicasEspeciales + "- " + caracteristica + "\n"  
        else: 
            "- " + caracteristica + "\n"
        return stateCaracteristicas
