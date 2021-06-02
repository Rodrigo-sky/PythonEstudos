def maiusculas(frase):
   
   lis_frase = frase.split()
   print(lis_frase)
   letras = ''

   for item in lis_frase:
      for letra in item:
         if (ord(letra) in range(64,91)):
            letras += letra
   return(letras)
   pass

print(maiusculas('PrOgRaMaMoS em python!'))