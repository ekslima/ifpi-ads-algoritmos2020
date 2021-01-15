def main():
    # entrada
    x = float(input("Coordenada x: "))
    y = float(input("Coordenada y: "))

    # processamento: Matemática + Condicionais + Repetições
    quadrante(x,y)

    # saída
    

def quadrante(x,y):
    if x > 0.0 and y > 0.0:
        print("Q1")
    elif x < 0.0 and y > 0.0:
        print("Q2")
    elif x < 0.0 and y < 0.0:
        print("Q3")
    elif x > 0.0 and y < 0.0:
        print("Q4")
    elif x == 0.0 and y == 0.0:
        print("Origem")
    elif x > 0.0 and y == 0.0:
        print("Eixo X")
    elif x == 0.0 and y > 0.0:
        print("Eixo Y")
    elif x < 0.0 and y == 0.0:
        print("Eixo X")
    elif x == 0.0 and y < 0.0:
        print("Eixo Y")


main()