def mutate_string(string, position, character):
    lista = list(string)
    for item in lista:
        if(lista[position] == item):
            lista[position] = character
    string = ''.join(lista)
    return(string)
    



string = 'abracadabra'
position = 5
character = 'k'

print(mutate_string(string, position, character))