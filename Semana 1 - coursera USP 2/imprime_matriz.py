def imprime_matriz(matriz):
   for i in matriz:
      for x in i:
         if (x == i[-1]):
            print(x,end="")
         else:
            print(x, end=" ")
      print("")

         

minha_matriz = ([[1, 2, 7], [3, 4, 8], [1, 2, 3]])
imprime_matriz(minha_matriz)