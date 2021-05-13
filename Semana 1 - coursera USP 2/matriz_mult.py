def sao_multiplicaveis(m1, m2):
   if len(m1[0]) == len(m2):
      return True
   else:
      return False


   pass



m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[2, 3, 4], [5, 6, 7]]
print(sao_multiplicaveis(m1, m2))