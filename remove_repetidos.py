def remove_repetidos (lista):
    
    if (len(lista) > 1):
        lista.sort()
        print(lista)
        elemento_anterior = lista[-1]

        for i in lista:
            if (i == elemento_anterior):
                del lista[]
                print("lista", lista)
            else:
                elemento_anterior = i
    else:
        return lista
        


lista = [12, 14, 12, 12, 13, 13, 11]

print(remove_repetidos(lista))