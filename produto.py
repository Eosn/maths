def produto(a, b):
   quo = a
   prod = 0
   if a%2 == 1:
       prod += b
   while quo != 1:
       quo = quo//2
       b = b*2
       if quo%2 == 1:
           prod += b
   return prod
