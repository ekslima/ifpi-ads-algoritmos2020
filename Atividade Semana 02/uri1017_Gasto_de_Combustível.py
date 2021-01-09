def main():
    # entrada
    tempo = int(input("Tempo gasto em horas: "))
    velocidade = int(input("Velocidade media em km/h: "))

    # processamento: Matemática + Condicionais + Repetições
    distancia = tempo * velocidade
    consumo = distancia / 12

    # saída
    print("Consumo em litros: %.3f" % consumo)


main()