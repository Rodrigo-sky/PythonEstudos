def find_string(str,sub_str):
   tam_sub = len(sub_str)
   vezes = 0
   for i in range(0,len(str)+1): #+1 para pegar a ultima letra
      print(f'verificando {sub_str}: Teste: {str[i:(i+tam_sub)]}')
      if (sub_str in str[i:(i+tam_sub)]): #Nem lembro disso rsrs; O str[i:(i+tam_sub) vai verificar cada conjunto pedido pelo usuario. Descomente o print acima para log (ou refrescar memoria rsrs)
         # print(str[i:(i+tam_sub)])
         vezes += 1
   return(vezes)
         #return(vezes)
      # else:
         # print(str[i:(i+tam_sub)])
   

print(find_string('ABABABALILILALIALIBABA', 'BABA'))