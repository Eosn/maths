def f_EhTriangulo():
   a = int(input("A: "))
   b = int(input("B: "))
   c = int(input("C: "))
   if ((a < b+c) and (b < a+c) and (c < a+c)):
       print("Os valores inseridos formam um triângulo.")
   else:
       print("Os valores inseridos não formam um triângulo.")
