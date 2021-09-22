def fibonacci(f):
   if f < 2:
      return f
   else:
      return fibonacci(f - 1) + fibonacci(f - 2)

#print(fibonacci(int(input())))