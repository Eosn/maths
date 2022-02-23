def digvf(num):
   digv = 0
   j = 2
   for i in range(len(num)-1, -1, -1):
       digv += int(num[i])*j
       j += 1
   digv = 11 - (digv%11)
   if (digv == 10) or (digv == 11):
       digv = 0
   return str(digv)
 
def main():
   nome = input("Nome (enter para cancelar): ")
   while nome != "":
       cpf = int(input("CPF: "))
       digv = digvf(str(cpf)[:-2]) + digvf(str(cpf)[:-1])
       if (str(cpf)[-2:] == digv):
           print("VÁLIDO.")
       else:
           print("INVÁLIDO.")
       nome = input("Nome (enter para cancelar): ")
