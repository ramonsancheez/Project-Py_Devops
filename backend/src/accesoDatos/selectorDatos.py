
# Función que recibe una baseDatos y una categoria, y devuelve la lista con todos los elementos con la misma categoria
def selector_Datos(baseDatos, categoria):
    coleccion = baseDatos.menus_with_schema
    # "lista" con todos los documentos con la misma categoria
    documentos = coleccion.find({"category":categoria})

    try:
        listaDiccionarios = []
        # Añadimos cada item a listaDiccionarios para obtener una lista con cada item
        for documento in documentos:
            listaDiccionarios.append(documento)
        if len(listaDiccionarios) == 0:
            raise ValueError 
    except:
        print("La colección de datos se encuentra vacía \n")
        exit()
    else:
        return listaDiccionarios