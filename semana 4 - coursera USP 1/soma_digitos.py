numInt = input("Digite um número inteiro:")
soma = 0
teste = len(numInt)  # verifica se tem apenas 1 numero
numInt = int(numInt)  # transforma em inteiro para a seguinte logica
if (teste == 1):
    soma = soma + (numInt % 10)
else:
    while(numInt % 10 != numInt):
        soma = soma + (numInt % 10)
        numInt = numInt // 10
    if (numInt % 10 == numInt):
        soma = soma + (numInt % 10)

print(soma)
