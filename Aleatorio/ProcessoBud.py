def sequencia (entrada):
   lista = []
   seq = ''
   numero = list(map(int, str(entrada)))

   for i in range(len(numero)-1):
         
      if numero[i]+1 == numero[i+1]:
         seq += str(numero[i])
         if i+1 == len(numero)-1:
            seq += str(numero[i+1])
            lista.append(int(seq))
      
      elif numero[i] == 9 and numero[i+1] == 0:
         seq += '9'
         if i+1 == len(numero)-1:
            seq += str(numero[i+1])
            lista.append(int(seq))
      
      else:
         if numero[i]-1 == numero[i-1]:
            seq += str(numero[i])
            lista.append(int(seq))
            seq = ''

   return max(lista)
