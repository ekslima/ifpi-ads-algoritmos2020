def main():
    # entrada
    entrada = input()
    partes1 = entrada.split()
    codigo_peca_1 = int(partes1[0])
    numero_de_pecas_1 = int(partes1[1])
    valor_peca_1 = float(partes1[2])

    entrada = input()
    partes2 = entrada.split()
    codigo_peca_2 = int(partes2[0])
    numero_de_pecas_2 = int(partes2[1])
    valor_peca_2 = float(partes2[2])

    # processamento: Matemática + Condicionais + Repetições
    TOTAL = (numero_de_pecas_1 * valor_peca_1) + (numero_de_pecas_2 * valor_peca_2)

    # saída
    print("VALOR A PAGAR: R$ %.2f" %(TOTAL))


main()