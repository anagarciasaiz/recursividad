lista = [1, 3, 5, 12, 27, 56, 78, 90]
limite_derecho = len(lista) - 1
limite_izquierdo = 0
numero = 9

def busqueda(lista, limite_derecho, limite_izquierdo, numero):  
    index = (limite_derecho + limite_izquierdo) // 2
    if lista[index] == numero:
        print("encontrado en:", index)
    elif lista[index] > numero:
        limite_derecho = index - 1  
        busqueda(lista, limite_derecho, limite_izquierdo, numero)
    else:
        limite_izquierdo = index + 1 
        busqueda(lista, limite_derecho, limite_izquierdo, numero)
        
busqueda(lista, limite_derecho, limite_izquierdo, numero)
