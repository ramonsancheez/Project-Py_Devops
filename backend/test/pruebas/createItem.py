def createItem(coleccion, newItem, respuesta):
    try:
        lowRespuesta = respuesta.lower()
        if lowRespuesta == "s":
            coleccion.insert_one(newItem)
            print("Se añadió el ítem correctamente")
        else:
            raise ValueError
    except:
        print("No se añadió nada a la colección")
        return False
    else:
        print("Se añadió a la colección")
        return True