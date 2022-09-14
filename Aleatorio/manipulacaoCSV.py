import csv
#abre o csv e exibe os casos de covid maior q 1
with open('Aleatorio/brasil_covid.csv','r', encoding= 'utf-8') as arquivo_csv:
   leitor = csv.reader(arquivo_csv)                               
   next(leitor)
   for linha in leitor:
      if float(linha[2]) > 1:
         print(linha)
   print('-----------------')

with open('Aleatorio/user.csv', 'w' , encoding= 'utf-8', newline='') as arquivo_users:
   escritor = csv.writer(arquivo_users)
   escritor.writerow(['nome', 'sobrenome', 'email', 'genero'])
   escritor.writerow(['Rodrigo', 'Teixeira', 'email.com', 'Masculino'])

with open('Aleatorio/user.csv', 'r' , encoding= 'utf-8', newline='') as arquivo_users:
   leitor = csv.reader(arquivo_users)
   for linha in leitor:
      print(linha)

print('-------------------------------------------------------------------------------------------------------------------------')

cabecalho = ['nome', 'sobrenome']
dados = []
opcao = input('O que deseja fazer?\n1 - Cadastrar\n0 - Sair\n')
while opcao != '0':
   nome = input('Qual o seu nome?')
   sobrenome = input('Qual o seu sobrenome?')
   dados.append([nome, sobrenome])
   opcao = input('O que deseja fazer?\n1 - Cadastrar\n0 - Sair\n')

print(dados)

with open('Aleatorio/user.csv', 'w' , encoding= 'utf-8', newline='') as arquivo_users:
   escritor = csv.writer(arquivo_users)
   escritor.writerow(cabecalho)
   escritor.writerows(dados)

with open('Aleatorio/user.csv', 'r' , encoding= 'utf-8', newline='') as arquivo_users:
   leitor = csv.reader(arquivo_users, delimiter=',')
   for linha in leitor:
      print(linha)