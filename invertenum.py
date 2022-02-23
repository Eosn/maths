def f_NumeroInverso():
    n = int(input("n: "))
    u = n // 100
    i = n % 100
    d = (i // 10)*10
    c = (i % 10)*100
    m = c + d + u
    return m
