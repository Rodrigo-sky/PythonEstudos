largura = int(input("digite a largura "))
altura = int(input("digite a altura "))
aux = largura
auxdois = altura

while altura > 0:
    while largura > 0:
        if (altura == 1 or altura == auxdois):
            print("#", end="")
        else:
            if(largura == 1 or largura == aux):
                print("#", end="")
            else:
                print(" ", end="")
        largura = largura - 1
    print()
    altura = altura -1 
    largura = aux