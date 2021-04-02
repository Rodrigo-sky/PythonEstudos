def remove_repetidos(lista):
   #input("teste")
   lista_dois = []
   for i in range(0, len(lista)):
      if(lista[i] not in lista_dois):
         lista_dois.append(lista[i])
      lista_dois.sort()
   return(lista_dois)


lista = [7,3,33,12,3,3,3,7,12,100]

print(remove_repetidos(lista))
