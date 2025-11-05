"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_02():
    lista_registros = {}
    with open("files/input/data.csv", "r") as data:
        for line in data:
            columnas = line.strip().split("\t")
            if columnas[0] not in lista_registros:
                lista_registros[columnas[0]] = 1
            else:
                lista_registros[columnas[0]] += 1
        
        lista_odenada = sorted(lista_registros.items())
        
        return lista_odenada

#print(pregunta_02())


"""
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

"""
