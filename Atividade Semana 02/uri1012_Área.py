def main():
    # entrada
    entrada = input()
    partes = entrada.split()
    A = float(partes[0])
    B = float(partes[1])
    C = float(partes[2])

    # processamento: Matemática + Condicionais + Repetições
    pi = 3.14159
    triangulo = (A * C) / 2
    circulo = (C**2) * pi
    trapezio = ((A + B) * C) / 2
    quadrado = B * B
    retangulo = A * B

    # saída
    print('TRIANGULO: %.3f' % triangulo)
    print('CIRCULO: %.3f' % circulo)
    print('TRAPEZIO: %.3f' % trapezio)
    print('QUADRADO: %.3f' % quadrado)
    print('RETANGULO: %.3f' % retangulo)


main()