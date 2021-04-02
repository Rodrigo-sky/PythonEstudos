numero = []
while 0 not in numero:
   numero.append(int(input('digite um numero: ')))
numero.remove(numero[-1])
numero.reverse()
for i in range(0, len(numero)):
   print (numero[i])