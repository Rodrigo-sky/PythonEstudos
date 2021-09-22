def soma_lista(lista, soma = 0):
   #input()
   if len(lista) == 1:
      soma += lista[0]
      return soma
   else:
      soma = soma + lista[0]
      lista.remove(lista[0])
      return soma_lista(lista, soma)
   pass

# liusta = [3] #23

# print(soma_lista(liusta))