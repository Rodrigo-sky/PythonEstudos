def e_hipotenusa(num):
    teste = input("teste")
    i = 1
    k = 1
    while i < num:
        while k < num:
            
            print("num", num**2)
            print("i", i**2)
            print("k", k**2)
            if (num**2 == i**2 + k**2):
                return True
            k = k + 1
        i = i + 1
    return False

print(e_hipotenusa(25))


# def soma_hipotenusa(num):
