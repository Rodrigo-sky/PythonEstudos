def solve(s):
   print('nomeAntes:', s)
   nome = ''
   s.lower()
   frase = s.split()
   for item in frase:
      nome += item.capitalize()
      if(frase[-1] == item):
         nome += ""
      else:
         nome += " "
   print('nomeDps:',nome )
   return(nome)

teste = '132 456 Wq  m e'