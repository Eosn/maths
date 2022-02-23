def f_capicua(n):
    n = str(n)
    inv = ""
    for i in range(len(n)):
        inv = n[i] + inv
    inv = int(inv)
    n = int(n)
    if inv == n:
        return True
    else:
        return False
