from pymongo import MongoClient
import certifi

def createItem():
    try:
        cluster = MongoClient('mongodb+srv://m001-student:mongo123@cluster0.qmgmx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority', tlsCAFile=certifi.where())
        baseDatos = cluster.proyecto
        coleccion = baseDatos.menus_with_schema
        newItem = { "titulo": "John", "stock":37, "price":3.99, "descriptionMenu": "Highway 37", "ingredients":["hola","soy", "ramon"], "category":"ComidaChatarra", "state":{"energy":34, "radiation":23, "toxicity":34}}

        respuesta = input(f"Va a añadir {newItem} a la base de datos, si desea cambiar los datos, hágalo en el editor de texto. ¿Desea añadir ese ítem? (S/N): ")
        lowRespuesta = respuesta.lower()
        if lowRespuesta == "s":
            coleccion.insert_one(newItem)
        else:
            raise ValueError
    except:
        print("No se añadió nada a la colección")
        exit()
    else:
        print("Se añadió el ítem correctamente")
        exit()
        
createItem()
