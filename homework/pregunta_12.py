"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    diccionario = {

    }
    with open("files/input/data.csv", "r") as data:
        for fila in data:
            renglon = fila.strip().split("\t")
            valores_juntos = renglon[4].split(",") #  [jjj:12,bbb:3,ddd:9,ggg:8,hhh:2]
            clave = renglon[0] #String de la columna 1
            for valoresSumar in valores_juntos: #iterar elemento de columna 5 y sumarlos
                suma = 0
                suma += int(valoresSumar[4:])
                if clave not in diccionario:
                    diccionario[clave] = suma
                else:
                    diccionario[clave] += suma
    return diccionario
"""
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
