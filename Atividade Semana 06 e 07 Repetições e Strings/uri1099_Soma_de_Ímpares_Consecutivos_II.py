def main():
    N = int(input())
    i = 1

    while i <= N:
        linha = input()
        dados = linha.split()
        X = int(dados[0])
        Y = int(dados[1])
        soma = 0
        if X > Y:
            for j in range(Y+1, X):
                if j % 2 != 0:
                    soma = soma + j
        elif X < Y:
            for j in range(X+1, Y):
                if j % 2 != 0:
                    soma = soma + j
        elif X == Y:
            soma == 0
        i = i + 1

        print(soma)


main()