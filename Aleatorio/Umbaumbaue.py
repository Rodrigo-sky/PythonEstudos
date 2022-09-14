# def estrobogramatico(n):
#     resultado = []
#     for i in range(n+1):
#         if checaEstrobo(str(i)):
#             resultado.append(i)
#     return resultado


# def checaEstrobo(numero):
#         dic = {("0", "0"), ("1", "1"), ("2","2"), ("5","5"), ("6", "9"), ("8", "8"), ("9", "6")}
#         i = 0
#         j = len(numero)-1
#         for i in range(j+1):
#             if (numero[i], numero[j]) not in dic:
#                 return False
#             j -= 1
#         return True

# print(estrobogramatico(4866))

# def exibe_soma(parcela1,parcela2,soma):
#     print(" ", end= " ")
#     print(*parcela1, sep = ' ')
#     print("+", end= " ")
#     print(*parcela2, sep = ' ')
#     print("---"+"--"*digits_number)
#     print(*soma, sep = ' ')
    
# print(exibe_soma([1, 8, 2, 6, 7], [8, 0, 1, 5, 1],[0, 9, 8, 4, 1, 8]))