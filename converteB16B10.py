def f_base16_para_base10(nb16):
    exp = len(nb16) - 1
    nb10 = 0
    for i in range(len(nb16)):
        if nb16[i] == "A":
            nb10 += 10*(16**exp)
        elif nb16[i] == "B":
            nb10 += 11*(16**exp)
        elif nb16[i] == "C":
            nb10 += 12*(16**exp)
        elif nb16[i] == "D":
            nb10 += 13*(16**exp)
        elif nb16[i] == "E":
            nb10 += 14*(16**exp)
        elif nb16[i] == "F":
            nb10 += 15*(16**exp)
        else:
            nb10 += int(nb16[i])*(16**exp)
        exp -= 1
    return nb10
