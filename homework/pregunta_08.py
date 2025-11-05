"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    with open("files/input/data.csv", "r") as data:
        diccionario = {}
        lista = []
        for renglon in data:
            column = renglon.strip().split("\t")
            numero, letra = column[1], column[0]
            if numero not in diccionario:
                diccionario[numero] = [letra] #si no está agregue numero
            else:               
                diccionario[numero].append(letra) #si ya está añada nueva letra
        for numero,lista_letras in diccionario.items():
            repetidas = set(lista_letras) #eliminar repetidos
            repetidas = list(repetidas)
            repetidas.sort()
            añadir = (int(numero), list(repetidas)) #cambiar formato a lista
            lista.append(añadir)
        lista.sort()
        return lista
    
#print(pregunta_08())

"""
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']), 
     (9, ['A', 'B', 'C', 'E'])]

    """
