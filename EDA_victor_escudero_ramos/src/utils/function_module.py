def createArray(citympg, highwaympg):
    '''
    Esta funcion recibe dos arrays como argumentos. Devuelve un array con la media de los dos arrays anteriores.
    '''
    array = []

    for i, j in zip(citympg, highwaympg):

        x = (i + j) / 2

        array.append(x)

    return array