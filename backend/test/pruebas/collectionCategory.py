def selector_Datos(coleccion, categoria):
    documentos = coleccion.find({"category":categoria})
    try:
        listaDiccionarios = []
        for documento in documentos:
            listaDiccionarios.append(documento)
        if len(listaDiccionarios) == 0:
            raise ValueError 
    except:
        print("La colección de datos se encuentra vacía")
        return False
    else:
        return True