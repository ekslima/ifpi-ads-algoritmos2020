def main():
    # entrada
    X = int(input("Distancia total em km: "))
    Y = float(input("Combustivel gasto: "))

    # processamento: Matemática + Condicionais + Repetições
    consumo = X / Y

    # saída
    print('%.3f km/l' % consumo)


main()