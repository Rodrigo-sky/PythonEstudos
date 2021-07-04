def ordena(lista):

   for i in range(len(lista)):
      mini = i                                           #"seleciona" o indice a ser ordenado e guarda em variavel para ser comparado
      for j in range(i, len(lista)):                     #itera segunda vez para checar os itens seguintes
         if lista[j] < lista[mini]:                      #compara cada item se ele eh menor
            mini = j                                     #Caso seja define o indice como menor
      if i != mini:                                      #Se o indice inicial nao conferir depois da checagem
         lista[i], lista[mini] = lista[mini] , lista[i]  #Troca os numeros pelos indices
   return lista                                          #Retorna a lista ordenada
      
         


lista  = [35, 51, 80, 92, 4]
print(ordena(lista))