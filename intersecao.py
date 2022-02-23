def naoEstaContido(l, s): #elimina duplicidade
    for i in range(len(s)):
        if (l == s[i]):
            return False
    return True

def intesc(s1, s2): #faz interseção
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
                    if (naoEstaContido(maior[j], s3)):
                        s3 += menor[i] + " "
    s3 += str(len(s3))
    return s3

def main(): #testado
    for i in range(1, 31):
        print("----- PAR %i DE STRINGS -----" % i)
        s1 = input("String 1: ").upper()
        s2 = input("String 2: ").upper()
        print("   Interseção: ", intersc(s1, s2))
