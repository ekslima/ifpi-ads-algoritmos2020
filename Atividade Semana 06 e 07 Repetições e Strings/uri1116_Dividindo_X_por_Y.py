def main():
    N = int(input())
    i = 1

    while i <= N:
        linha = input()
        dados = linha.split()
        X = int(dados[0])
        Y = int(dados[1])

        if Y == 0:
            print("divisao impossivel")
        else:
            divisao = X / Y
            print("%.1f" % divisao)
        i = i + 1


main()