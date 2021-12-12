from accesoDatos.selectorDatos import selector_Datos
from .ingredientsArray import ingredientsList
from .stateCaracteristicas import stateCaracteristicas  
import os

# Función que pasa el item recibido dentro del archivo recibido también con formato md
def escritorMarkdown(documento, archivo):
    for key in documento:
        string = ""
        valor = documento[key]
        # Utilizamos un "switch", ya que es más eficaz que los if's
        match key:
            case "_id":
                continue
            case "titulo":
                string += "# " + str(valor)
            case "descriptionMenu":
                string += str(valor)
            case "stock":
                string += "Stock disponible: " + str(valor) + " unidades"
            case "price":
                string += "El precio es de: " + "**" + str(valor) + "€**"
            case "ingredients":
                string = ingredientsList(documento)
            case "state":
                string = stateCaracteristicas(documento)
            case "category":        
                string += "La categoria es: " + "**" + str(valor) + "**"
        # Escribe el string correspondiente en el archivo
        archivo.write(string + "\n" + "\n")

# Le pasamos la baseDatos y una categoria, especificada en el main
def creadorMarkdown(baseDatos, categoria):
    # Crea una carpeta llamada archivosMarkdown, y, al cambiar de categoria, no la vuelve a crear y no salta error
    os.makedirs("./archivosMarkdown", exist_ok=True)
    listaDiccionarios = selector_Datos(baseDatos, categoria)
    # De selector_Datos obtenemos la lista con los nueve items
    i = 0
    # Abre un archivo con el nombre de la categoria, extensión .md
    archivo = open("./archivosMarkdown/" + categoria + ".md", "w", encoding="utf-8")
    # i es la posicion dentro de listaDiccionarios, y  i = 0, es el primer item de los nueve que hay en la lista 
    while i < len(listaDiccionarios):
        escritorMarkdown(listaDiccionarios[i], archivo)
        i += 1
    # Cuando finaliza listaDiccionarios cierra el archivo
    archivo.close()