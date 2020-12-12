def main():
    # entrada
    nome_funcionario = input("Nome do funcionario: ")
    salario_fixo = float(input("Salario fixo: "))
    total_vendas = float(input("Total de vendas no mes: "))

    # processamento: Matemática + Condicionais + Repetições
    TOTAL = salario_fixo + (total_vendas * 0.15)

    # saída
    print("TOTAL = R$ %.2f" %(TOTAL))


main()