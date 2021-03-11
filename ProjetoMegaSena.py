#projeto de app pra sortear numeros
import random

numerosSorteio = []

for i in range(0,6):
	numerosSorteio.insert(i,random.randint(0,60))
	
print()
print("Os numeros da ''sorte'' são:")
print(numerosSorteio)