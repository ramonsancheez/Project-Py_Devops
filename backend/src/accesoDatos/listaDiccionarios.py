import pymongo

def selector_Datos(baseDatos, categoria):
    coleccion = baseDatos.menus_with_schema
    documentos = coleccion.find({"category":categoria})

    listaDiccionarios = []
    for documento in documentos:
        listaDiccionarios.append(documento)
    return listaDiccionarios