def conta_letras(frase, contar="vogais"):
   vogais = ['a', 'e', 'i', 'o', 'u']
   cont_vogal = 0
   cont_conso = 0
   new_frase = frase.lower()
   if (contar == 'consoantes'):
      for item in new_frase:
         if ((item not in vogais) and (ord(item) in range(97,123))): #range para numero decimal de ord()
            cont_conso +=1
      return (cont_conso)
      #print (f'o tamanho total é {len(frase)}\n consoantes são {cont_conso}')
   else:
      for item in new_frase:
         if (item in vogais):
            cont_vogal +=1
      return (cont_vogal)
      #print(f'o tamanho total é {len(frase)}\n vogais são {cont_vogal}')

print(conta_letras('programamos em {{ python'))