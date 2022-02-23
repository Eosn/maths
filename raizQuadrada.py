def f_calcula_raiz_quadrada(n):
    raiz = n/2
    for i in range(2, 21):
        raiz = (raiz**2 + n)/(2*raiz)
    return raiz
