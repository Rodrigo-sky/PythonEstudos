numero = input("Digite um número inteiro:")
Pnultimo = 0
qtdDigito = len(numero)                #conta as casas de q o numero vai ter 
numero = int(numero) 
                   
if qtdDigito>1:                        #se tiver mais de uma casa executa o loop de resto ja retorna a negativa
    while qtdDigito >= 1:
        Pnultimo = ((numero%100) // 10) #numero dividido por 100 retorna as duas ultimas casas e o 10 para excluir a ultima casa restando a penultima
        if (Pnultimo == numero%10):     #Se o pnultimo numero for igual ao ultimo numero %10 para extrair o ultimo numero
            print("sim")
            break
        elif numero%10 == numero:       #Se chegar no ultimo numero e nao encontrar numero igual retorna a negativa inves de simplesmente fechar o programa
            print("não")
        numero = numero//10
        qtdDigito = qtdDigito-1
else:
    print("não")