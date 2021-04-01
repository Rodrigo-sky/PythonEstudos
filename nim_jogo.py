def computador_escolhe_jogada(n,m):
   aux = 1 
   while(aux <= m):
      restantes = n - aux
      if (restantes % (m+1) == 0):
         print(f'O computador tirou {aux} peças.')
         return aux
      aux = aux + 1
   if (n <= m):
      print(f'O computador tirou {n} peças.')
      return n
   else:
      print(f'O computador tirou {m} peças.')
      return m

def usuario_escolhe_jogada(n,m):
   jogada = int(input('Quantas peças você vai tirar? '))
   while jogada > 0:
      if jogada > n:
         print('Oops! Jogada inválida! Tente de novo.')
         jogada = int(input('Quantas peças você vai tirar? '))
      else:
         if jogada <= m and jogada > 0:
            print(f'Voce tirou {jogada} peças.')
            return jogada
         else:
            print('Oops! Jogada inválida! Tente de novo.')
            jogada = int(input('Quantas peças você vai tirar? '))

def partida():
   n = int(input('Quantas peças? '))
   m = int(input('Limite de peças por jogada? '))
   jogador_vez = True
   pc_vez = True

   if (n % (m+1) == 0):
      pc_vez = False
      print(f'Voce começa!\n ')
   else:
      jogador_vez = False
      print(f'Computador começa!\n ')
   while (n >= 0):
      if jogador_vez == True:
         jogada_user = usuario_escolhe_jogada(n,m)
         n = n - jogada_user
         if n >= 1:
            print(f'Agora restam {n} peças no tabuleiro.\n')
         else:
            print(f'Fim do jogo!\n')
            return('Voce ganhou!')
         jogador_vez = False
         pc_vez = True
      else:
         jogada_pc = computador_escolhe_jogada(n,m)
         n = n - jogada_pc
         if n >= 1:
            print(f'Agora restam {n} peças no tabuleiro.\n')
         else:
            return('O computador ganhou!')
         pc_vez = False
         jogador_vez = True

def campeonato():
   print(f'Voce escolheu Campeonato\n')
   score_user = 0
   score_pc = 0
   aux = 0

   while aux < 3:
      print(f'\n**** Rodada {aux+1} ****\n')
      resultado = partida()
      if resultado == 'Voce ganhou!':
         score_user += 1
      else:
         score_pc += 1
      aux += 1
   print(f'**** Final do campeonato! ****\nPlacar: Você {score_user} X {score_pc} Computador')
         
def Main():
   print('Bem-vindo ao jogo do NIM! Escolha:\n')
   escolha = int(input(f'\n1 - para jogar uma partida isolada\n2 - para jogar um campeonato '))
   if (escolha == "1"):
      partida()
   elif (escolha != 1 and escolha != 2):
      print('\nOops! Escolha inválida! Tente de novo.')
      escolha = int(input(f'\n1 - para jogar uma partida isolada\n2 - para jogar um campeonato '))
   else:
      campeonato()
         

Main()