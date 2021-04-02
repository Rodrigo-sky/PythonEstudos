numero = input("digite um numero")  # recebe o numero
tamanho = len(numero)  # verifica a quantidade de de tamanho
operador = 0  # inicializa a "operação"
numero = int(numero)  # converte a variavel pra numero

while tamanho >= 1:  # enquanto a quantidade de numero for superior a 1 executa o codigo
    # executa a operação somando a cada loop
    operador = operador + (numero % 10)
    numero = numero // 10  # retira o numero para nao somar mais de uma vez
    tamanho = tamanho - 1  # retira a quantidade pra dar sequencia ao loop
print(operador)  # print maroto
