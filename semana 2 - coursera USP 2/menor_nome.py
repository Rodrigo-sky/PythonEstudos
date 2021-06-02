def menor_nome(nomes):
   sla = []
   for item in nomes:
      sla.append(item.strip())
   aux = sla[0]
   for item in sla:
      if(len(item) < len(aux)):
         aux = item
   aux = aux.capitalize()
   return aux
      
   
   pass

menor_nome(['maria', 'josé', 'PAULO', 'Catarina'])