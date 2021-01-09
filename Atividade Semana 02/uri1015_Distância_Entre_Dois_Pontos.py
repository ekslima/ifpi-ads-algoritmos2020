import math

def main():
    # entrada
    entrada = input()
    partes1 = entrada.split()
    x1 = float(partes1[0])
    y1 = float(partes1[1])
    
    entrada = input()
    partes2 = entrada.split()
    x2 = float(partes2[0])
    y2 = float(partes2[1])

    # processamento: Matemática + Condicionais + Repetições
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    # saída
    print('%.4f' % distancia)


main()