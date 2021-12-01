from accesoDatos.conexionBasedatos import lista

# def convert_dict_to_md(self, output_fn):
#         with open(output_fn, 'w') as writer:
#             writer.writelines(self.mddata)
#         print('Dict successfully converted to md')

def markdown(diccionarioDiccionario):
    # i hace referencia a la posición que del documento en el diccionario
    i = 0 
    while i < len(diccionarioDiccionario):
        bucle(diccionarioDiccionario[i])
        i += 1