def main():
    # entrada
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    n3 = float(input("Nota 3: "))
    n4 = float(input("Nota 4: "))

    # processamento: Matemática + Condicionais + Repetições
    media_ponderada = (n1*2 + n2*3 + n3*4 + n4*1) / (2 + 3 + 4 + 1)

    # saída
    resultado_final(media_ponderada)


def resultado_final(media):
    print("Media: %.1f" % media)
    if media >= 7.0:
        print("Aluno aprovado.")
    elif media < 5.0:
        print("Aluno reprovado.")
    elif media >= 5.0 and media <= 6.9:
        print("Aluno em exame.")
        nota_exame = float(input("Nota do exame: "))
        print("Nota do exame: %.1f" % nota_exame)
        media_final(nota_exame,media)


def media_final(exame,media):
    media_recalculada = (exame + media) / 2
    if media_recalculada >= 5.0:
        print("Aluno aprovado.")
        print("Media final: %.1f" % media_recalculada)
    else:
        print("Aluno reprovado.")
        print("Media final: %.1f" % media_recalculada)


main()