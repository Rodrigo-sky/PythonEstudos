def dimensoes(matriz):
   tam = len(matriz)
   for i in matriz:
      col = len(i)
   print(f'{str(tam)}x{col}')
      
minha_matriz = [[1, 2, 3], [4, 5, 6]]
dimensoes(minha_matriz)