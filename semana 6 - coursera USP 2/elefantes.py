def incomodam(n):
   if n > 0:
      return n * "incomodam "
   else:
      return ""

   pass

#print(incomodam(int(input()))) #WORKING

def elefantes(n, max = None):
   # if max == None:
   #    max = n
   
   if n >= 1:
      if n == 1:
         return "Um elefante incomoda muita gente\n"
      else:
         # if n == max:
         #    n = n - 1
         #return elefantes(n-1, max) + str(n) + " elefantes incomodam muita gente\n"+str(n+1)+" elefantes "+incomodam(n+1)+"muito mais\n"      
         return elefantes(n-1) + str(n) + " elefantes " + incomodam(n) + "muito mais\n" + str(n) + " elefantes incomodam muita gente\n"
   else:
      return ""

   pass

print(elefantes(int(input())))

