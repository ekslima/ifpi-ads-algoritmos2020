def main():
    # entrada
    entrada = input()
    partes = entrada.split()
    A = float(partes[0])
    B = float(partes[1])
    C = float(partes[2])

    # processamento: Matemática + Condicionais + Repetições
    maiorAB = (A + B + abs(A - B)) / 2
    maiorAB = (maiorAB + C + abs(maiorAB - C)) / 2

    # saída
    print('%d eh o maior' % maiorAB)


main()