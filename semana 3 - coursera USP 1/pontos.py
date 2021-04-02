import math
pontoX1 = float(input("Insira o PRIMEIRO ponto referente a x "))
PontoY1= float(input("Insira o PRIMEIRO ponto referente a y "))
pontoX2 = float(input("Insira o SEGUNDO ponto referente a x "))
PontoY2= float(input("Insira o SEGUNDO ponto referente a y "))
distancia = math.sqrt(((pontoX1 - pontoX2) **2)+((PontoY1 - PontoY2) **2))
if distancia >=10:
    print("longe")
else:
    print("perto")