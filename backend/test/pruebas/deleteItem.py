def deleteItem(coleccion, respuesta, deletedItem):
    try:
        lowRespuesta = respuesta.lower()
        if lowRespuesta == "s":
            coleccion.delete_one(deletedItem)
        else:
            raise ValueError
    except:
        print("No se puedo eliminar el item")
        return False
    else:
        print("Se eliminó el item de la colección")
        return True
    # coleccion.delete_many({"name": "John"}) #Elimina todos los items que tengan key NAME y valor Mr.GenericTraceback
    # coleccion.remove() Elimina todos los ítems
    # coleccion.delete_one(deletedItem) Elimina ese item
