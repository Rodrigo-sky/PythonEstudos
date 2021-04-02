def maior_elemento(lista):
   #input("teste")
   maior_item = lista[0]
   for i in range(0, len(lista)):
      if lista[i] > maior_item:
         maior_item = lista[i]
   return(maior_item)
   
lista = [-90, -27, -12]
maior_elemento(lista)
