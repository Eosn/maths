def f_divisores(n): #retorna a quantidade de divisores
    cont = 1
    for i in range(1, 1+n//2):
        if n%i == 0:
            cont += 1
    return cont
