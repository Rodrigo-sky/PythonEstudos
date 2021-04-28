import re

def le_assinatura():
   '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
   print("Bem-vindo ao detector automático de COH-PIAH.")
   print("Informe a assinatura típica de um aluno infectado:")

   wal = float(input("Entre o tamanho médio de palavra:"))
   ttr = float(input("Entre a relação Type-Token:"))
   hlr = float(input("Entre a Razão Hapax Legomana:"))
   sal = float(input("Entre o tamanho médio de sentença:"))
   sac = float(input("Entre a complexidade média da sentença:"))
   pal = float(input("Entre o tamanho medio de frase:"))

   return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
   '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
   i = 1
   textos = []
   texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
   while texto:
      textos.append(texto)
      i += 1
      texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

   return textos

def separa_sentencas(texto):
   '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
   sentencas = re.split(r'[.!?]+', texto)
   if sentencas[-1] == '':
      del sentencas[-1]
   return sentencas

def separa_frases(sentenca):
   '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
   return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
   '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
   return frase.split()

def n_palavras_unicas(lista_palavras):
   '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
   freq = dict()
   unicas = 0
   for palavra in lista_palavras:
      p = palavra.lower()
      if p in freq:
         if freq[p] == 1:
               unicas -= 1
         freq[p] += 1
      else:
         freq[p] = 1
         unicas += 1

   return unicas

def n_palavras_diferentes(lista_palavras):
   '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
   freq = dict()
   for palavra in lista_palavras:
      p = palavra.lower()
      if p in freq:
         freq[p] += 1
      else:
         freq[p] = 1

   return len(freq)

def compara_assinatura(as_a, as_b):
   '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
   pass

def calcula_assinatura(texto):
   input('gay')
   print("--------------------------------------------------------------------------------------")
   '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
   #tam_med_pal = 0 #soma dos tamanhos das palavras dividida pelo número total de palavras.
   # type_token_rel = 0 #número de palavras diferentes dividido pelo número total de palavras.
   # rel_hapax_lego = 0 #número de palavras que aparecem uma única vez dividido pelo total de palavras.
   sentece = separa_sentencas(texto)
   tam_med_sentence = 0
   sentence_complex = 0
   tam_med_frase = 0
   aux = 0
   frases = []

   for i in range(len(sentece)):
      tam_med_sentence = tam_med_sentence + len(sentece[i])
      print("\ntamanho da sentença ",tam_med_sentence)
      # ------------------------------------------------------------------
      sentence_complex = sentence_complex + len(separa_frases(sentece[i]))
      print(f'complexidade | frases totais {sentence_complex} \n')
      #-------------------------------------------------------------------
      frases = frases + separa_frases(sentece[i])
      for aux in range(len(frases)):
         tam_med_frase = tam_med_frase + len(frases[aux])
         print(f'tamanho de caracteres da frase é {tam_med_frase}')
      #-------------------------------------------------------------------
   
   # rel_hapax_lego = rel_hapax_lego /
   tam_med_sentence = tam_med_sentence / (i+1)
   sentence_complex = sentence_complex / (i+1)
   tam_med_frase = tam_med_frase / (aux+1)
   
   print(f'\nTamanho médio de sentença: {tam_med_sentence}')
   print(f'Complexidade de sentença: {sentence_complex}')
   print(f'Tamanho médio de frase: {tam_med_frase}')
   # return tam_med_sentence
   # return sentence_complex
   pass
   



def avalia_textos(textos, ass_cp):
   '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
   pass


#textos para teste

texto1 = "a peppa disse para o coelho: Coelho tu é um baita de um filho da puta sabia?"
texto2 = " the peppa Said to the rabbit: Coelho, tu é muito cuzão zé " 
texto4 = "NxZero é uma banda de emocore gay formada em meados de 2005, quando um pobre morador gay de rua chamado Josefino Nogueira achou um violão podre na rua, faltavam 4 cordas, e ele percebeu que com essas 2 cordas ele podia fazer 4039 músicas diferentes com o mesmo ritmo. Andando pelas ruas, faminto e com vontade de dar, ele para no supermercado e se encontra com Silvio Santos que humildemente tira sua carteira recheada de barras de ouro, e lhe paga um X-Miseria (Pão com pão e nada dentro)."
texto3 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
# print( separa_frases(separa_sentencas(texto3)[0]))
# print( separa_palavras(separa_frases(separa_sentencas(texto3)[0])[0]))
calcula_assinatura(texto3)

#AS FUNÇÕES PRE FEITAS GERAM LISTAS  DE CADA SEQUENCIA, ENTAO TENHO QUE FAZER UM LOOP DE CADA FUNÇÃO PARA CALCULAR A MEDIA DAS MESMAS