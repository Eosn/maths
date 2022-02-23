def euler(n):
    e = 0
    den = 1
    for i in range(1, n+1): #n!
        e+= 1/(den)
        den = den*i
    return e

def main3_4_15():
    n = 1
    while (exp(1)-e) >= 0.0001: #como calcular exp(1)????
        e = euler(n)
        n += 1
    print(n)
