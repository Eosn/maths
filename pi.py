def pi(n):
    den = 0
    op = 1
    cont = 1
    base = 1
    s = 0
    while cont <= n:
        den = base**3
        if (op%2 == 0):
            s -= 1/den
        else:
            s += 1/den
        op += 1
        cont += 1
        base += 2
    pi = (s*32)**(1/3)
    print("N = %i    Pi = %.5f" % (n, pi))

def main3_4_14(): #testado (questão 2 da prova 1)
    n = int(input("N: "))
    if n <= 0:
        print("N = %i      N INVALIDO" % (n))
    else:
        for i in range(1, n+1):
            pi(i)
