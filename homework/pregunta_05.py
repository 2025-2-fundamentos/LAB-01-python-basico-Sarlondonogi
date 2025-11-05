"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    diccionario = {}
    with open("files/input/data.csv", "r") as data:
        for renglon in data:
            column = renglon.strip().split("\t")
            if column[0] not in diccionario:
                diccionario[column[0]] = [column[0],int(column[1]),int(column[1])]
            elif column[0] in diccionario:
                if int(column[1]) > int(diccionario[column[0]][1]):
                    diccionario[column[0]][1] = int(column[1])
                elif int(column[1]) < int(diccionario[column[0]][2]):
                    diccionario[column[0]][2] = int(column[1])
    lista = []
    for letra, tuplas in diccionario.items():
        lista.append(tuple(tuplas))
    lista.sort()
    return lista


"""
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
