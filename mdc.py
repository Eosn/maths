def f_calcula_mdc_recursiva(n, m):
    if (m == 0):
        return n
    else:
        return f_calcula_mdc(m, n%m)

def f_calcula_mdc(n, m):
    while (m != 0):
        r = n%m
        n = m
        m = r
    return n
