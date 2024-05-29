def bubble(lista):
    
    for index in range(len(lista)):
        for x in range(0, len(lista) - index - 1):
            if (lista[x] > lista[x+1]):
                lista[x], lista[x+1] =lista[x + 1], lista[x]
    
    return lista

def bubble2(lista):
    
    for index in range(len(lista)):
        for x in range(0, len(lista) - index - 1):
            if (lista[x] < lista[x+1]):
                lista[x], lista[x+1] =lista[x + 1], lista[x]
    
    return lista

list = [58, 64, 4, 23, 6, 15, 1]
print(bubble(list))
print(bubble2(list))


