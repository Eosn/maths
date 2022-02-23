def EhPalindromo():
    frase = input("Digite algo: ")
    frase2 = ""
    for i in range(len(frase)):
        if frase[i] != " ":
            frase2 = frase2 + frase[i]
    if frase2.upper() == frase2[::-1].upper():
        print(frase, " é palíndromo.")
    else:
        print(frase, " não é palíndromo.")
