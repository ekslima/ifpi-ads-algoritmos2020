def main():
    # entrada
    idade = int(input("Idade em dias: "))

    # processamento: Matemática + Condicionais + Repetições
    anos = idade // 365
    meses = (idade % 365) // 30
    dias = (idade % 365) % 30

    # saída
    print('%d ano(s)' % anos)
    print('%d mes(es)' % meses)
    print('%d dia(s)' % dias)


main()