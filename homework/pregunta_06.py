"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():

    with open("files/input/data.csv", "r") as data:
        diccionario = {}
        for renglones in data:
            columna = renglones.strip().split("\t") #Separar los renglones
            columna[4] = list(columna[4].split(",")) #convierte en lista y separa por comas
            for palabra in columna[4]: 
                elemento = str(palabra[0:3]) #separar el string de 3 letras
                numero = int(palabra[4:]) #separar el numero 
                if elemento not in diccionario: #si no esta en el diciconario agregarlo
                    tupla = [elemento, numero, numero]
                    diccionario[elemento] = tupla
                else: #definir max y min
                    if numero > diccionario[elemento][2]:
                        diccionario[elemento][2] = numero
                    elif numero < diccionario[elemento][1]:
                        diccionario[elemento][1] = numero
    lista = []
    for i,j in diccionario.items(): #convertir formato letra : tupla
        lista.append(tuple(j))
    lista.sort()
    return lista
#print(pregunta_06())


"""
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

"""
