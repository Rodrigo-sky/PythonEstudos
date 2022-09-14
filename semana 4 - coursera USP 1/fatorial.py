valorN = int(input("Digite o valor de n:"))  # recebe o numero
multiplicação = 1  # inicia a variavel com 1 pois se trata do operador de multiplicação

while(valorN > 1):  # enquanto o numero for maior que 1 executa o loop do fatorial
    #operador = valorN * (valorN - 1)
    # vai armazenar o resultado e executar a operação
    multiplicação = multiplicação * valorN
    valorN = valorN-1  # vai reduzindo os numeros da sequencia de fatorial

print(multiplicação)  # print maroto
