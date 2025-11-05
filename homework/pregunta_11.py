"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    diccionario = {

    }
    with open("files/input/data.csv", "r") as data:
        for fila in data:
            renglon = fila.strip().split("\t")
            numero_suma = int(renglon[1])
            for letra in renglon[3].split(","):
                #si no está agregarlo
                if letra not in diccionario:
                    diccionario[letra] = numero_suma
                else:
                    diccionario[letra] += numero_suma
    return diccionario

"""
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


"""
