def main():
    N = int(input())
    media_ponderada(N)


def media_ponderada(valor):
   contador = 0
   while contador < valor:
       linha = input()
       dados = linha.split()
       nota1 = float(dados[0])
       nota2 = float(dados[1])
       nota3 = float(dados[2])
       media = ((2 * nota1) + (3 * nota2) + (5 * nota3)) / (2 + 3 + 5)
       print("%.1f" % media)
       contador = contador + 1

main()