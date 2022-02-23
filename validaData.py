def validaData(dia, mes, ano):
    dia, mes, ano = int(dia), int(mes), int(ano)
    if (ano%400 == 0) or ((ano%4 == 0) and (ano%100 != 0)):
        m2 = 29
    else:
        m2 = 28
    if mes == 2:
        if dia > m2:
            return False
    elif (mes == 4) or (mes == 6) or (mes == 9) or (mes == 11):
        if dia > 30:
            return False
    else:
        if dia > 31:
            return False
    return True

def mesExt(mes):
    if mes == "01":
        mes = "Janeiro"
    elif mes == "02":
        mes = "Fevereiro"
    elif mes == "03":
        mes = "Março"
    elif mes == "04":
        mes = "Abril"
    elif mes == "05":
        mes = "Maio"
    elif mes == "06":
        mes = "Junho"
    elif mes == "07":
        mes = "Julho"
    elif mes == "08":
        mes = "Agosto"
    elif mes == "09":
        mes = "Setembro"
    elif mes == "10":
        mes = "Outubro"
    elif mes == "11":
        mes = "Novembro"
    elif mes == "12":
        mes = "Dezembro"
    return mes

def mainData(): #testado (questão 6 APNP7.2)
    datNum = input("Data de nascimento (DD/MM/AAAA): ")
    dia = datNum[:2]
    mes = datNum[3:5]
    ano = datNum[6:]
    while (validaData(dia, mes, ano) == False) :
        print(" --- Data inválida. ---")
        datNum = input("Data de nascimento (DD/MM/AAAA): ")
        dia = datNum[:2]
        mes = datNum[3:5]
        ano = datNum[6:]
    mes = mesExt(mes)
    print("Você nasceu em %s de %s de %s." % (dia, mes, ano))
