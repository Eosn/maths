def primeira(d):
    if (d == 7) or (d == 11):
        return "Natural"
    if (d == 2) or (d == 3) or (d == 12):
        return "Craps"
    if (d == 4) or (d == 5) or (d == 6) or (d == 8) or (d == 9) or (d == 10):
        return "Ponto"

def ponto(d, i):
    if (d == 7):
        return False
    elif (d == i):
        return True
    else:
        return "Repete"

def dados():
    d1 = int(input("D1: "))
    d2 = int(input("D2: "))
    d = d1 + d2
    while (d < 2) or (d > 12):
        print("Valor(es) informado(s) inválido(s).")
        d1 = int(input("D1: "))
        d2 = int(input("D2: "))
        d = d1 + d2
    return d

def mainCraps():
    d = dados()
    if (primeira(d) == "Natural"):
        print("Ganhou.")
    elif (primeira(d) == "Craps"):
        print("Perdeu.")
    elif (primeira(d) == "Ponto"):
        print("Ponto. ---------")
        i = d
        d = dados()
        p = ponto(d, i)
        while (p == "Repete"):
            d = dados()
            p = ponto(d, i)
        if p:
            print("Ganhou.")
        else:
            print("Perdeu.")
