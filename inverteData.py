def f_DataInverso():
    ent = int(input("Data: "))
    d = ent // 10000
    i = ent % 10000
    m = (i // 100)*100
    a = (i % 100)*10000
    sai = d + m + a
    return (d, m, a, sai)
