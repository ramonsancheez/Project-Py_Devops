import json
# Para poder realizar la conversión de un diccionario a json,
# importamos este módulo "json" de las librerias de python

from conexionBasedatos import lista 
datosDict = dict(lista)
print (datosDict)

def convertirEnJson(datosDict, ):

    with open('personal.json', 'w') as json_file:
        json.dump(datosDict, json_file, indent=4)

# "json.dumps" convierte el objeto python en una string de json, 
# para que podamos operar con esa string y llevar a cabo la conversión.


    with open('data.json', 'w') as fp:
        json.dump(dict, fp,  indent=4)
    print 
#como argumento le pasamos el diccionario python
# datosJson = json.dumps(datosDict)
# print (datosJson)
# def convertirEnJson(myRecord, filename):
#     """convert_json: Write a dictionary into a JSON file that we specified
#     Args:
#         myRecord (dict): It's a dictionary that we want write into JSON file
#         filename (str): Name of JSON file where dictionary will be written
#     Returns:
#         str: Return a string with a message with information about the result's process of function
#     """
    
#     #* PRECONDICIONALES
#     assert isinstance(myRecord, dict)
#     assert isinstance(filename, str)
    
#     mensaje = f"El diccionario ha sido convertido a json en este archivo: {filename}.json"
#     try:
#         # j = json.dumps(myRecord)
#         # para que pueda funcionar with open, la ruta empieza desde la raíz hasta la carpeta donde esta el archivo donde queremos guardar los datos
#         with open(f"backend/json/{filename}.json", "a", encoding="utf-8") as f: 
#             x = json.dumps(myRecord, indent=4)
#             f.write(x + ',' + '\n')
#             # f.close()
#     except json.JSONDecodeError as jsonerror:
#         mensaje = "Decoding json ha fallado" 
#     except FileNotFoundError as notfile:
#         mensaje = "Archivo no encontrado"
#     except Exception as exc:
#         print("Ha ocurrido un error: ", exc.args)
        
#     return mensaje


if __name__ == "__main__":
    print(convertirEnJson.__doc__)