def main():
    # entrada
    numero = int(input("Numero do funcionario: "))
    horas = int(input("Horas trabalhadas: "))
    valor_hora = float(input("Valor da hora: "))

    # processamento: Matemática + Condicionais + Repetições
    SALARIO = horas * valor_hora

    # saída
    print("NUMERO =", numero)
    print("SALARIO = U$ %.2f" %(SALARIO))


main()