# def mutate_string(string, position, character):
#     lista = list(string)
#     for item in lista:
#         if(lista[position] == item):
#             lista[position] = character
#     string = ''.join(lista)
#     return(string)
    



# string = 'abracadabra'
# position = 5
# character = 'k'

# print(mutate_string(string, position, character))

# -----------------------------------------------------------------------------
from ntpath import join
import string
from unittest import result
# import string

# def print_rangoli(size):
    
    
#     for i in range((size*2)-1):                     #loop vertical
#         alpha = string.ascii_lowercase[0:size]      #import da biblioteca de str para alfabeto
#         for x in range((size*2)-1):                 #loop horizontal
            
#             if(x == (size*2)-2):                    #caso ultimo numero, imprima sem tracejado
#                 #print(alpha[x],end='')
#                 print((size*2)-2)
#             else:
#                 #print(alpha[x]+'-',end='')
#                 print((size*2)-2)
#         print()
        
#     pass



# def stringfy(ranger,size):
#     alphabet = string.ascii_lowercase[0:size]
#     alphabet = list(alphabet.strip(' '))

#     for i in range(1,ranger+1,2):
#         print(i)
#         if i == size:
#             print('é')
#         else:
#             ('nao é')
#     pass

#------------------------------------------------------------------------

def print_rangoli(size):
    alphabet = string.ascii_lowercase[0:size]
    alphabet = list(alphabet.strip(' '))
    alphabetmom = []
    esquerda = []
    junin = []
    for i in range((size*2)-1):                 #loop vertical

        if i >= size:                       #se i for passar da do tamanho do alfabeto pedido começa diminuir novamente
            if len(alphabetmom) > 2:        #se a lista tiver mais que um elemento vai imprimir do outro lado
                esquerda = alphabetmom[2:i]
                #print(list(reversed(esquerda)), end='')
            else:
                esquerda.pop()
            alphabetmom = alphabetmom[1:]

        elif i < size :                     #enquanto nao chegar na metade vai acrescentando ao alfabeto
            if len(alphabetmom) >= 1:        #se a lista tiver mais que um elemento vai imprimir do outro lado
                esquerda = alphabetmom[0:i]
                #print(list(reversed(esquerda)), end='')
            alphabetmom = alphabet[-i-1:]

        junin = list(reversed(esquerda)) + alphabetmom
        print('-'.join(junin).center((size*4)-3,'-'))
            
        #for j in range((size*2)-1):             #loop horizontal
        #    pass

        #print(junin)
#        print('-'.join(junin).center((size*2)-1, ' '))
    pass

            

print_rangoli(10)