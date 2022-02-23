def uniao(s1, s2): #une
    s3 = ""
    for i in range(len(s1)):
        if (naoExiste(s1[i], s3) and s1[i] != " "):
            s3 += s1[i] + " "
    for j in range(len(s2)):
        if (naoExiste(s2[j], s3) and s2[j] != " "):
            s3 += s2[j] + " "
    return s3

def naoExiste(l, s): #elimina duplicidade
    for i in range(len(s)):
        if (l == s[i]):
            return False
    return True

def compara(s1, s2): #faz interseção
    if (len(s1) > len(s2)):
        maior = s1
        menor = s2
    else:
        maior = s2
        menor = s1
    s3 = ""
    for i in range(len(menor)):
        for j in range(len(maior)):
            if (menor[i] != " " and maior[j] != " "):
                if (menor[i] == maior[j]):
                    if (naoExiste(maior[j], s3)):
                        s3 += menor[i] + " "
    return s3

def main():
    #s1 = "THE QUICK BROWN DOG JUMPS OVER THE LAZY FOX"
    #s2 = "LOREN IPSUM"
    for i in range(1, 51):
        print("----- PAR %i DE CONJUNTOS -----" % i)
        s1 = input("String 1: ").upper()
        s2 = input("String 2: ").upper()
        print("   Interseção: ", compara(s1, s2))
        print("   União: ", uniao(s1, s2))
