bandera= ["r","a","a","r","v","a","a","r","a","r","r","v","r","r","a","v","v"]
for i in range(len(bandera)):
    if bandera[i] == "r":
        bandera[i] = 0
    elif bandera[i] == "v":
        bandera[i] = 1
    else:
        bandera[i] = 2
        
        

def sort(lista, reorden = None):
    if reorden is None:
        reorden = []
    if len(lista) == 0:
        return reorden
    else:
        x = min(lista)
        lista.remove(x)
        reorden.append(x)
        return sort(lista, reorden)

bandera = sort(bandera)



for i in range(len(bandera)):
    if bandera[i] == 0:
        bandera[i] = "r"
    elif bandera[i] == 1:
        bandera[i] = "v"
    else:
        bandera[i] = "a"


print(bandera)