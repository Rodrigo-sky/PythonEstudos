def primo(x):
    aux = 2                             # variavel pro while
    divisiveis = 0                              # teste de condição pra ver se existe mais de 1 divisor

    while (aux <= x):              # enquanto o loop for acontecendo vai testando quantos numeros sao divisiveis
        if (x % aux == 0):
            divisiveis += 1
        aux = aux + 1
    
    if divisiveis == True:
        return True
    else:
        return False

def n_primos (x):
    cont = 0
    auxdois = 1
    if x >= 2:
        while auxdois <= x:
            if(primo(auxdois) == True):
                cont = cont + 1
            auxdois = auxdois + 1
        return(cont)
    else:
        return("numero invalido")
        
