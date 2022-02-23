def f_base10_para_base16(nb10):
    nb16 = ""
    while nb10 > 0:
        i = nb10%16
        if i == 10:
            i = "A"
        elif i == 11:
            i = "B"
        elif i == 12:
            i = "C"
        elif i == 13:
            i = "D"
        elif i == 14:
            i = "E"
        elif i == 15:
            i = "F"
        nb16 = str(i) + nb16
        nb10 = nb10//16
    if nb16 == "":
        return 0
    else:
        return nb16
