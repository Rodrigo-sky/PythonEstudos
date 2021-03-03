# recebe o numero variavel pra dar sequencia no loop pro encontro do impar
valorImpar = int(input("Digite o valor de n:"))
num = 0
impar = 0  # variavel pra controlar o impar a ser printado
# enquanto a variavel impar for menor q o numero pedido o loop é executado
while(impar < valorImpar):
    if (num % 2 != 0):  # se for nao for divisivel por '2'
        print(num)  # printa o impar
        impar = impar + 1                       # regula o impar
    num = num+1  # soma de qualquer modo
