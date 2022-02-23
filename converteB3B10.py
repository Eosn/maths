def f_base3_para_base10(nb3):
    nb3 = str(nb3)
    exp = len(nb3) - 1
    nb10 = 0
    for i in range(len(nb3)):
        nb10 += int(nb3[i])*(3**exp)
        exp -= 1
    return nb10
