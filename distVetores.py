def distvet(x, y):
    dist = 0
    for i in range(len(x)):
        dist += (int(x[i])-int(y[i]))**2
    dist**(1/2)
    return dist

def main():
    m = int(input("Quantos pares de vetores serão fornecidos? "))
    for i in range(1, m+1):
        print("--- PAR %i DE VETORES ---" % i)
        x = input("Vetor 1 [xyz...n]: ")
        y = input("Vetor 2 [xyz...n]: ")
        while len(x) != len(y):
            print("Os vetores devem possuir a mesma quantidade de lados.")
            x = input("Vetor 1 [xyz...n]: ")
            y = input("Vetor 2 [xyz...n]: ")
        dist = distvet(x, y)
        print("Distância: ", dist)
