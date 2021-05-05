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

   ass = 0
   for i in range(6):
      x = abs(as_a[i] - as_b[i])
      ass = ass + x
   ass = ass / 6
   return(ass)

def calcula_assinatura(texto):
   sentece = separa_sentencas(texto)
   tam_med_sentence = 0
   sentence_complex = 0
   tam_med_frase = 0
   tam_med_palavra = 0
   frases = []
   palavras = []

   for i in range(len(sentece)):
      tam_med_sentence = tam_med_sentence + len(sentece[i])
      sentence_complex = sentence_complex + len(separa_frases(sentece[i]))
      frases = frases + separa_frases(sentece[i])

   for x in range(len(frases)):
      tam_med_frase = tam_med_frase + len(frases[x])
      palavras = palavras + separa_palavras(frases[x])     
      
   for y in range(len(palavras)):
      tam_med_palavra = tam_med_palavra + len(palavras[y])
   tam_med_palavra = tam_med_palavra / (y+1)

   type_token_rel = n_palavras_diferentes(palavras)/ len(palavras)
   rel_hapax_lego = n_palavras_unicas(palavras)/ len(palavras)
   tam_med_sentence = tam_med_sentence / (i+1)
   sentence_complex = sentence_complex / (i+1)
   tam_med_frase = tam_med_frase / (x+1)

   return[tam_med_palavra, type_token_rel, rel_hapax_lego, tam_med_sentence, sentence_complex, tam_med_frase]

def avalia_textos(textos, ass_cp):
   '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
   aux = 1000000000
   esse = 0

   for i in range(len(textos)):
      ass_text = calcula_assinatura(textos[i])
      ass_comparada = compara_assinatura(ass_cp,ass_text)
      if ass_comparada <= aux:
         aux = ass_comparada
         esse = i

   return esse + 1

def main():
   ass_cp = le_assinatura()
   textos = le_textos()
   print(f'O autor do texto {avalia_textos(textos,ass_cp)} está infectado com COH-PIAH')

main()
