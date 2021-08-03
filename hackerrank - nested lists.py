if __name__ == '__main__':
   lista = []
   for i in range(int(input())):
      name = input()
      score = float(input())
      aux = [name, score]
      lista.append(aux)
   print(lista)
   mini = lista[0][1]
   for i in range(len(lista)):
      if lista[i][1] < mini:
         mini = lista[i] # lista[i][1]

# lista = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41.0], ['Harsh', 39.0]]





   
   


   
   