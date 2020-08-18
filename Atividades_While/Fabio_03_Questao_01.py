""" Questão 01: Leia N e escreva todos os números inteiros de 1 a N.
"""

def main():
    N = int(input("Numero inteiro: "))
    cont = 1

    while cont <= N:
        print(cont)
        cont = cont + 1

main()