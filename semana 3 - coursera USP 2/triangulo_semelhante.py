def main():
   t = Triangulo(18, 27, 15)
   t2 = Triangulo(6, 9, 5)
   print(t.a)
   print(t.b)
   print(t.c)
   print(t.perimetro())
   print(t.tipo_lado())
   print(t.retangulo())
   print(t.semelhantes(t2))
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
   
   def retangulo(self):
      if(self.a**2 == ((self.b**2)+(self.c**2))) or (self.b**2 == ((self.a**2)+(self.c**2))) or (self.c**2 == ((self.b**2)+(self.a**2))):
         return True
      else:
         return False

   def semelhantes(self, triangulo):
      t1 = [self.a, self.b, self.c]
      t2 = [triangulo.a, triangulo.b, triangulo.c]
      t1.sort()
      t2.sort()
      if ((t1[0]//t2[0]) == (t1[1]//t2[1]) and (t1[1]//t2[1]) == (t1[2]//t2[2])):
         return True
      else:
         return False
      
      

main()