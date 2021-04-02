def computador_escolhe_jogada(n,m):
    aux = 1 #int(input("teste"))
    while(aux <= m):
        restantes = n - aux
        if (restantes % (m+1) == 0):
            print("O computador tirou ", aux, "peças.")
            return (aux)
        aux = aux + 1
    
    if (n <= m):
        print("O computador tirou ", n, "peças.")
        return (n)
    else:
        print("O computador tirou ", m, "peças.")
        return (m)


def usuario_escolhe_jogada(n,m):
    jogada_valida = False
    while (jogada_valida == False):
        jogada = int(input("Quantas peças você vai tirar? "))
        if (jogada > n):
            print("Oops! Jogada inválida! Tente de novo.")
            usuario_escolhe_jogada(n,m)
        else:
            if (jogada <= m and jogada > 0 ):
                jogada_valida = True
                if jogada > 1:
                    print("Voce tirou", jogada, "peças.")
                    return jogada
                else:
                    print("Você tirou uma peça")
                return jogada
            else:
                print("Oops! Jogada inválida! Tente de novo.")


def campeonato ():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print()
    print("1 - para jogar uma partida isolada")
    escolha = input("2 - para jogar um campeonato ")
    score_pc = 0
    score_user = 0

    if (escolha == "1"):
        print("Voce escolheu uma partida isolada")
        print()
        # print(partida())
        if(partida() == "Fim do jogo! O computador ganhou!"):
            score_pc = score_pc + 1
            print()
            placar = "Placar: Você " + str(score_user) + " X " + str(score_pc) + " Computador"
            return(placar)
        else:
            score_user = score_user + 1
            print()
            placar = "Placar: Você " + str(score_user) + " X " + str(score_pc) + " Computador"
            return(placar)
    else:
        print("Voce escolheu um campeonato!")
        print()
        rodada = 1
        while(rodada <= 3):
            print("**** Rodada ",rodada ,"****")
            print()
            if(partida() == "Fim do jogo! O computador ganhou!"):
                score_pc = score_pc + 1
                print()
                placar = "Placar: Você " + str(score_user) + " X " + str(score_pc) + " Computador"
                print(placar)
                print()
            else:
                score_user = score_user + 1
                print()
                placar = "Placar: Você " + str(score_user) + " X " + str(score_pc) + " Computador"
                print(placar)
                print()
            rodada = rodada + 1
        return("**** Final do campeonato! ****")


def partida ():   
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    print("Obrigado!")
    primeira_jogador = True
    primeira_computador = True
    switch_jogador = True

    
    if (n % (m+1) == 0):        #testa a primeira jogada do player
        if primeira_jogador == True:
                primeira_jogador = False
                primeira_computador = False
                switch_jogador = True
                print("Voce começa!")
                print()
    else:                       #Primeira vez do PC
        if primeira_computador == True:
                primeira_jogador = False
                primeira_computador = False
                switch_jogador = False
                print("Computador começa!")
                print()      
    while(n >= 0):
        if switch_jogador == True:
            jogada_user = usuario_escolhe_jogada(n,m)
            n = n - jogada_user
            if(n <= 0):
                #vitoria_user = True
                return("Fim do jogo! Voce ganhou!")
            if n > 1:
                print("Agora restam", n, "peças no tabuleiro.")
                print()
            elif n== 1:
                print("Agora resta apenas uma peça no tabuleiro.")
                print()
            switch_jogador = False
        else:
            jogada_pc = computador_escolhe_jogada(n,m)
            n = n - jogada_pc
            if(n <= 0):
                #vitoria_pc = True
                print("Fim do jogo!\n")
                return("O computador ganhou!")
            if n > 1:
                print("Agora restam", n, "peças no tabuleiro.")
                print()
            elif n == 1:
                print("Agora resta apenas uma peça no tabuleiro.")
                print()
            switch_jogador = True
        
#print(partida())
usuario_escolhe_jogada(5,3)