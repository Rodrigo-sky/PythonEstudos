from os import read


arquivo = open('Aleatorio/dom_casmurro_cap_1.txt', 'r', encoding='utf8')         #abre o caminho do caminho. letra 'r' para ler
texto = arquivo.read()                                                           #le o arquivo e printa ele
print(texto)
arquivo.close()                                                                  #SEMPRE FECHAR O ARQUIVO

with open('Aleatorio/dom_casmurro_cap_1.txt', 'r', encoding='utf8') as arquivo:  #COM o arquivo aberto faça:.... fora do bloco o arquivo é automaticamente fechado
   texto = arquivo.read()
   print(texto)
#arquivo.read()                                                                   #Python se nega a ler pois o mesmo ja esta fechado

#caso o arquivo nao exista ele cria um novo.
with open('Aleatorio/escrita_teste.txt', 'w', encoding='utf8') as arquivo:       #o 'w' funciona paara escrever 
   arquivo.write('Teste teste, é o carro do ovo passando na sua rua \nÉ o carro da rua passando no seu ovo\n')

with open('Aleatorio/escrita_teste.txt', 'a', encoding='utf8') as arquivo:       #o 'a' funciona para dar um append
   arquivo.write('Nova Linha nessa caralha de texto porra!!')

with open('Aleatorio/escrita_teste.txt', 'r', encoding='utf8') as arquivo:
   print(arquivo.read(), end= '')