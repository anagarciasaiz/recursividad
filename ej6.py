frase = str(input('Introduzca una frase:'))

#funcion que elimina los acentos
def sustituir_acentos(car):
    if car == "á":
        return "a"
    elif car == "é":
        return "e"
    elif car == "í":
        return "i"
    elif car == "ó":
        return "o"
    elif car == "ú":
        return "u"
    else: 
        return car
    
    
def hazcadena(lista, cadena):
    if len(lista) != 0:
        car = lista.pop()
        cadena = hazcadena(lista, cadena)
        car = car.lower()
        if car != " ":
            cadena = cadena + sustituir_acentos(car)
    return cadena


def preparar_frase(frase):
    frase_tabla = list(frase)
    cadena = ""
    cadena = hazcadena(frase_tabla, cadena)
    return cadena

def es_palindromo(frase):
    # Se convierte la frase a minúsculas
    frase = frase.lower()
    # Se eliminan todos los caracteres que no sean letras
    frase = "".join(c for c in frase if c.isalpha())
    # Se comparan las letras al inicio y al final de la frase hasta que se crucen
    inicio = 0
    fin = len(frase) - 1
    while inicio < fin:
        if frase[inicio] != frase[fin]:
            return False
        inicio += 1
        fin -= 1
    return True


frase = preparar_frase(frase)
if es_palindromo(frase):
    print("Esta frase es palíndroma")
else:
    print("Esta frase no es palíndroma")


