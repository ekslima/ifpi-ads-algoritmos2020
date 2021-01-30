def main():
    cont = 0
    soma = 0
    while cont < 2:
        nota = float(input())
        if nota >= 0 and nota <= 10:
            soma = soma + nota
            cont = cont + 1
        else:
            print("nota invalida")
    media = soma / 2

    print("media = %.2f" % media)


main()