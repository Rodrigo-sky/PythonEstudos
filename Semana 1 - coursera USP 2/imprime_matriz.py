# def imprime_matriz(matriz):
#    for i in matriz:
#       for x in i:
#          print(x, end=" ")
#       print("")

def imprime_matriz(matriz):
   for i in matriz:
      for x in range(len(i)):
         print(i[x], end="")
         if x < len(i):
            print(" ",end="")
            
         

# minha_matriz = ([[1, 2, 7], [3, 4, 8], [1, 2, 3]])
# imprime_matriz(minha_matriz)