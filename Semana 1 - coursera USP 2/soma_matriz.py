def soma_matrizes(m1, m2):

   if (len(m1) != len(m2)):
      return False
   else:
      matriz = []
      for i in range(len(m1)):
         if (len(m1[i]) != len(m2[i])):
            return False
         linha = []
         for x in range(len(m1[i])):
            linha.append(m1[i][x] + m2[i][x])
         matriz.append(linha)
      return matriz


# m1 = [[1, 2, 3], [4, 5, 6]]
# m2 = [[2, 3, 4], [5, 6, 7]]

# soma_matrizes(m1, m2)
 