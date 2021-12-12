def updateItem(coleccion, respuesta, updateItem):
    try:
        lowRespuesta = respuesta.lower()
        if lowRespuesta == "s":
            coleccion.update_one(updateItem,{"$set":{"descriptionMenu":"Comida riquisima"}})
        else:
            raise ValueError
    except:
        print("El item noo se pudo actualizar")
        return False
    else:
        print("Se actualizó correctamente")
        return True  