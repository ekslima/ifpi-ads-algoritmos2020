def main():
    # entrada
    N = int(input())
    print(N)

    # processamento: Matemática + Condicionais + Repetições
    notas_100 = N // 100
    N = N - notas_100 * 100

    notas_50 = N // 50
    N = N - notas_50 * 50

    notas_20 = N // 20
    N = N - notas_20 * 20

    notas_10 = N // 10
    N = N - notas_10 * 10

    notas_5 = N // 5
    N = N - notas_5 * 5

    notas_2 = N // 2
    N = N - notas_2 * 2

    notas_1 = N // 1
    N = N - notas_1 * 1

    # saída
    print('%d nota(s) de R$ 100,00' % notas_100)
    print('%d nota(s) de R$ 50,00' % notas_50)
    print('%d nota(s) de R$ 20,00' % notas_20)
    print('%d nota(s) de R$ 10,00' % notas_10)
    print('%d nota(s) de R$ 5,00' % notas_5)
    print('%d nota(s) de R$ 2,00' % notas_2)
    print('%d nota(s) de R$ 1,00' % notas_1)


main()