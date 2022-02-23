def f_eqQuadratica():
   a = float(input("A: "))
   if a != 0:
       b = float(input("B: "))
       c = float(input("C: "))
       delta = b**2 - 4*a*c
       if (delta < 0):
           print("Não há raizes reais.")
       elif (delta > 0):
           x1 = (-b + delta**0.5)/2*a
           x2 = (-b - delta**0.5)/2*a
           print("X1 = ", x1, "; X2 = ", x2)
       else:
           x1 = -b/2*a
           print("X = ", x1)
   else:
       print("Valor de A inválido.")
