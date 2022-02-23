def f_OrdenaNums():
   a = int(input("A: "))
   b = int(input("B: "))
   c = int(input("C: "))
   if (a < b and a < c):
       if (c < b):
           aux = c
           c = b
           b = aux
   else:
       if (b < c):
           aux = b
           b = a
           a = aux
           if (c < b):
               aux = c
               c = b
               b = aux
       else:
           aux = c
           c = a
           a = aux
           if (c < b):
               aux = c
               c = b
               b = aux
   print(a, b, c)
