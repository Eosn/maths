def ex_21(): #testado
   nome = input("Nome: ")
   altura = float(input("Altura (metros): "))
   sexo = input("Sexo (M/F): ").upper()
   pIdeal = 0.0
   if (sexo == "M"):
       pIdeal = (72.7 * altura) - 58
   elif (sexo == "F"):
       pIdeal = (62.1 * altura) - 44.7
   print("O peso ideal para ", nome, " é de ", pIdeal, "kg.")
