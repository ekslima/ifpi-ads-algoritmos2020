def main():
    contador = 0
    maior = 0
    posicao = 0
    while contador < 100:
       valor = int(input())
       contador = contador + 1
       if valor > maior:
           maior = valor
           posicao = contador
    print(maior)
    print(posicao)

main()