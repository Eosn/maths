def f_ComparaStrings():
    s1 = input("String 1: ")
    t1 = len(s1)
    s2 = input("String 2: ")
    t2 = len(s2)
    print("Tamanho de '", s1, "': ", t1, "caracteres.")
    print("Tamanho de '", s2, "': ", t2, "caracteres.")
    if (t1 == t2):
        print("As duas strings possuem o mesmo tamanho.")
        if (s1 == s2):
            print("As duas strings possuem o mesmo conteúdo.")
        else:
            print("As duas strings possuem conteúdos diferentes.")
    else:
        print("As duas strings são de tamanhos diferentes. As duas strings possuem conteúdos diferentes.")
