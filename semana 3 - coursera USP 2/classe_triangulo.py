def main():
   t = Triangulo(6,3,6)
   print(t.a)
   print(t.b)
   print(t.c)
   t.perimetro()

class Triangulo:
   def __init__(self, a, b, c):
      self.a = a
      self.b = b
      self.c = c
   
   
   def perimetro(self):
      perimetro = (self.a + self.b + self.c)
      return perimetro

main()