def ehprimo(n):
    for d in range(2, (n//2)+1): #maior div inteiro de um número é sua metade
        if n%d == 0:
            return False
    return True
