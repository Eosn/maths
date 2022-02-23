def f_base10_para_base3(nb10):
    exp = 0
    #nb3 = ""
    nb3 = 0
    while nb10 > 0:
        i = nb10 % 3
        #nb3 = str(i) + nb3
        nb3 += i*(10**exp)
        nb10 = nb10//3
        exp += 1
    '''if nb3 == "":
        return 0
    else:'''
    return int(nb3)
