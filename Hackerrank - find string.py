def find_string(str,sub_str):
   # print(f'{str}\n{sub_str}')
   tam_sub = len(sub_str)
   vezes = 0
   for i in range(0,len(str)+1):
      print(str[i:(i+tam_sub)])
      if (sub_str in str[i:(i+tam_sub)]):
         # print(str[i:(i+tam_sub)])
         vezes += 1
         print(vezes)
         #return(vezes)
      # else:
         # print(str[i:(i+tam_sub)])
   

find_string('ABCDCDC', 'CDC')