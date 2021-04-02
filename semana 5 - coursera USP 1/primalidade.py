print("o numero é primo?")                  # boas vindas
numero = int(input("digite o numero: "))    # pede o numero ao usuario
testeDeLoop = 2                             # variavel pro while
divisiveis = 0                              # teste de condição pra ver se existe mais de 1 divisor

while (testeDeLoop <= numero):              # enquanto o loop for acontecendo vai testando quantos numeros sao divisiveis
    if (numero % testeDeLoop == 0):
        divisiveis += 1
    testeDeLoop = testeDeLoop + 1

if (divisiveis == 1):
    print("primo")
else:                                       # qualquer outro numero deixa de ser primo
    print("não primo")