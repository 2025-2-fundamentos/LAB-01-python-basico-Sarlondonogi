"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    lista = []
    with open("files/input/data.csv", "r") as data:
        for fila in data:
            renglon = fila.strip().split("\t")
            letra, elementos_1, elementos_2 = renglon[0], len(renglon[3].split(",")), len(renglon[4].split(","))
            lista.append((letra, elementos_1, elementos_2))

    return lista

"""
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
