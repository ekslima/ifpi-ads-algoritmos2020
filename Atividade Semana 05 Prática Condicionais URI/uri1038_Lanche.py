def main():
    # entrada
    cod = int(input("Codigo do produto: "))
    quant = int(input("Quantidade: "))

    # processamento: Matemática + Condicionais + Repetições
    conta_total(cod, quant)

    # saída
   

def conta_total(n1,n2):
    if n1 == 1:
        total = n2 * 4.00
        print("Total: R$ %.2f" % total)
    elif n1 == 2:
        total = n2 * 4.50
        print("Total: R$ %.2f" % total)
    elif n1 == 3:
        total = n2 * 5.00
        print("Total: R$ %.2f" % total)
    elif n1 == 4:
        total = n2 * 2.00
        print("Total: R$ %.2f" % total)
    elif n1 == 5:
        total = n2 * 1.50
        print("Total: R$ %.2f" % total)


main()