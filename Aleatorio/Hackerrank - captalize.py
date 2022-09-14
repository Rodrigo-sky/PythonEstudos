def solve(s):
    s.lower()
    nome = ''
    frase = s.split(' ')

    for item in frase:
        nome += item.capitalize()
        if(frase[-1] == item.lower()):
            nome += ""
        else:
            nome += " "
    return nome

teste = '132 456 Wq      m e'
print(solve(teste))