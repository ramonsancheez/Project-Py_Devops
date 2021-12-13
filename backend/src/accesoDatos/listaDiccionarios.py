def selector_Datos(baseDatos, categoria):
    coleccion = baseDatos.menus_with_schema
    documentos = coleccion.find({"category":categoria}, {">_id" : False})

    try:
        listaDiccionarios = []
        for documento in documentos:
            listaDiccionarios.append(documento)
        if len(listaDiccionarios) == 0:
            raise ValueError 
    except:
        print("La colección de datos se encuentra vacía \n")
        exit()
    else:
        return listaDiccionarios