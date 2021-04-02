def testePrimo(numero):
    testeDeLoop = 1                             # variavel pro while
    divisiveis = 0                              # teste de condição pra ver se existe mais de 1 divisor

    while (testeDeLoop <= numero):              # enquanto o loop for acontecendo vai testando quantos numeros sao divisiveis
        if (numero % testeDeLoop == 0):
            divisiveis = divisiveis + 1
        testeDeLoop = testeDeLoop +1
    if divisiveis == 2:
        return True
    else:
        return False

def maior_primo (numero):
    if(testePrimo(numero) == True):
        return numero
    else:
        aux = 2
        primo = 0
        while (aux < numero):
            if (testePrimo(aux) == True):
                primo = aux
            aux = aux + 1
        return primo


#print(maior_primo (101))