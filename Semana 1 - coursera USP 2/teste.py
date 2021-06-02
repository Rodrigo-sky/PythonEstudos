
s = '12abc'
# input()
nome = ''
frase = s.split()
for item in frase:
    nome += item.capitalize()
    if(frase[-1] == item):
        nome += ""
    else:
        nome += " "
print(nome, type(nome))