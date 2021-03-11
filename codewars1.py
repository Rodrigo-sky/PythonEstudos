# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

# Note: The function accepts an integer and returns an integer


def square_digits(num): #recebe o numero
    
    #inicialização de variaveis
    numberQuadrado = None
    aux = len(str(num)) 
    i = 0
    lista = []
    

    #loop para adição a uma lista
    while i <= (aux-1):
            
            numberQuadrado = (num%10) * (num%10)
            lista.insert(i,str(numberQuadrado))
    
            num = num//10
            i = i + 1

    #ordenar e retorno
    lista.reverse()
    lista = ''.join(lista)
    lista = int(lista)

    return (lista)

print(square_digits(24351))
# teste square