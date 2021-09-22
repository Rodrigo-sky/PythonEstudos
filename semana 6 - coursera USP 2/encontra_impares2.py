def encontra_impares(lista, lista_impar = None):
   #inicializa a lista com os numeros impares
   if lista_impar == None:
      lista_impar = []

   

   
#se a lista for igual a 1 ou menor ja termina a recursao
   if len(lista)+1 < 2:
      return(lista_impar)
   if lista[0] % 2 != 0: #verifica se o numero é impar, caso seja adiciona na lista impar e remove da lista dada para dar continuidade e recursao
      lista_impar.append(lista[0])
      lista.remove(lista[0])
      return encontra_impares(lista,lista_impar) 
   else: #caso seja par so vai remover o numero da lista para permitir a recursao dos proximos numeros da lista
      lista.remove(lista[0])
      return encontra_impares(lista,lista_impar)

   

liusta = [2]
# liusta = [-9, 4, 5, -8, -7]
print(encontra_impares(liusta))
