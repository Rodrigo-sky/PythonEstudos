largura = int(input("digite a largura "))
altura = int(input("digite a altura "))

aux = largura
while altura > 0:
    while largura > 0:
        print("#", end="")
        largura = largura - 1
    print()
    altura = altura -1 
    largura = aux