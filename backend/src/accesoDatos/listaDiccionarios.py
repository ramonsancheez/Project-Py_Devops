import pymongo

def selector_Datos(baseDatos, categoria):
    coleccion = baseDatos.menus_with_schema
    documentos = coleccion.find({"category":categoria})

    try:
        listaDiccionarios = []
        for documento in documentos:
            listaDiccionarios.append(documento)
        assert listaDiccionarios 
    except:
        print("La colección de datos se encuentra vacía")
        exit()
    else:
        return listaDiccionarios