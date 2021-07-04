def busca(lista, elemento):
   if elemento not in lista:
      return False
   else:
      #return lista.index(elemento)
      for i in range(len(lista)):
         if lista[i] == elemento:
            return i
         
   
   pass

lista = ['a', 'e', 'i']

elemento = 'e'
print(busca(lista, elemento))