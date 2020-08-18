""" Questão 02: Leia N e escreva todos os números inteiros pares de 1 a N.
"""

def main():
    N = int(input("Numero inteiro: "))
    cont = 1

    while cont <= N:
        if cont % 2 == 0:
            print(cont)
        cont = cont + 1

main()