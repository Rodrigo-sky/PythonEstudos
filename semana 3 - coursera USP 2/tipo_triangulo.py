def main():
   t = Triangulo(2,3,6)
   print(t.a)
   print(t.b)
   print(t.c)
   print(t.perimetro())
   print(t.tipo_lado())
class Triangulo:
   def __init__(self, a, b, c):
      self.a = a
      self.b = b
      self.c = c
   
   
   def perimetro(self):
      perimetro = (self.a + self.b + self.c)
      return perimetro
   
   def tipo_lado(self):
      if((self.a != self.b) and (self.b != self.c) and (self.a != self.c)):
         return 'escaleno'
      elif((self.a == self.b) and (self.b == self.c) and (self.a == self.c)):
         return 'equilátero'
      else:
         return 'isósceles'

main()