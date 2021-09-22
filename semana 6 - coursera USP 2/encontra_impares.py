def encontra_impares(lista, teste = [], recursao = None):
   if recursao == None:
      recursao = len(lista) - 1
   #teste.extend(encontra_impares(lista))
   if lista[recursao] // 2 != 0:
      teste.append(lista[recursao])

   pass
   



liusta = [3, 6, 4, 7, 3, 8]
print(encontra_impares(liusta))

#nao to sabendo estruturar a recursão para executar o laço


