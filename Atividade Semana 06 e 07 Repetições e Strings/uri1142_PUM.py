def main():
	N = int(input())
	contador = 0
	quant = 0
	while contador < N:
		print(quant+1, end=' ')
		print(quant+2, end=' ')
		print(quant+3, end=' ')
		print("PUM")
		
		quant = quant + 4
		contador = contador + 1

main()