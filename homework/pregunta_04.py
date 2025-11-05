"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    meses = {}
    with open("files/input/data.csv", "r") as data:
        for linea in data:
            column = linea.strip().split("\t")
            fecha = column[2].split("-")
            if fecha[1] not in meses:
                meses[fecha[1]] = 1
            else:
                meses[fecha[1]] += 1
        meses_ordenados = sorted(meses.items())
        return meses_ordenados

#print(pregunta_04())

"""
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
    ('02', 4),
    ('03', 2),
    ('04', 4),
    ('05', 3),
    ('06', 3),
    ('07', 5),
    ('08', 6),
    ('09', 3),
    ('10', 2),
    ('11', 2),
    ('12', 3)]

"""
