class Banco:
   #Construtor
   def __init__(self, cliente, saldo, ):
      self.cliente = cliente
      self.saldo = saldo
      
   #Metodo
   def saque(self, valor):
      if valor > self.saldo:
         print('Operacao invalida!')
      else:
         self.saldo = self.saldo - valor
         print('O Cliente ',self.cliente, 'fez um saque de valor', valor, 'restando ', self.saldo)
      return self.saldo

   def deposito(self, valor):
      self.saldo = self.saldo + valor
      print('O Cliente ',self.cliente, 'fez um deposito de valor', valor, 'restando ', self.saldo)
      return self.saldo

   def imprimeSaldo(self):
      print('O Cliente ',self.cliente, 'tem um saldo de valor', self.saldo)

conta = Banco('Rogerio',1500)

conta.imprimeSaldo()
saldo = conta.saque(1600)
