def main():
    # entrada
    N = int(input("Tempo em segundos: "))

    # processamento: Matemática + Condicionais + Repetições
    horas = N // 3600
    minutos = (N % 3600) // 60
    segundos = N % 60

    # saída
    print('Em horas, minutos e segundos: %d:%d:%d'% (horas,minutos,segundos))


main()