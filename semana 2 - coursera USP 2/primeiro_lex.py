def primeiro_lex(lista):
   lex = lista[0]
   for i in range(len(lista)):
      if (lista[i] < lex): #precisa ser menor devido a ordem decimal, onde o primeiro é menor
         lex = lista[i]
   return(lex)


print(primeiro_lex(['oĺá', 'A', 'a', 'casa']))