def qtddias(d, m, a):
   d = int(d)
   m = int(m)
   a = int(a)
   n = d
   for i in range(1, m):
       if i == 2:
           if (a%400 == 0) or ((a%4 == 0) and (a%100 != 0)):
               n += 29
           else:
               n += 28
       elif (i == 4) or (i == 6) or (i == 9) or (i == 11):
           n += 30
       else:
           n += 31
   return n
 
def validadata(data):
   dia = int(data[:1])
   mes = int(data[2:4])
   ano = int(data[-4:])
   if (ano < 0) or (mes > 12):
       return False
   if (ano%400 == 0) or ((ano%4 == 0) and (ano%100 != 0)):
       m2 = 29
   else:
       m2 = 28
   if (mes == 4) or (mes == 6) or (mes == 9) or (mes == 11):
       if dia <= 30:
           return True
       else:
           return False
   elif mes == 2:
       if dia <= m2:
           return True
       else:
           return False
   else:
       if dia <= 31:
           return True
       else:
           return False
 
def main():
   print("Digite 0 em qualquer uma das datas para sair.")
   data1 = input("Data 1 (ddmmaaaa): ")
   data2 = input("Data 2 (ddmmaaaa): ")
   while (int(data1) != 0) and (int(data2) != 0):
       if (validadata(data1)) and (validadata(data2)) and (data1[-4:] ==data2[-4:]):
           qtd1 = qtddias(data1[:1], data1[2:4], data1[-4:])
           qtd2 = qtddias(data2[:1], data2[2:4], data2[-4:])
           dif = qtd1-qtd2
           if dif < 0:
               dif = dif*(-1)
           print("Há uma diferença de %i dias entre %s e %s." % (dif, data1, data2))
       else:
           print("DATA(S) INCORRETA(S). Datas inseridas: %s e %s." % (data1, data2))
       print("\nDigite 0 em qualquer uma das datas para sair.")
       data1 = input("Data 1 (ddmmaaaa): ")
       data2 = input("Data 2 (ddmmaaaa): ")
