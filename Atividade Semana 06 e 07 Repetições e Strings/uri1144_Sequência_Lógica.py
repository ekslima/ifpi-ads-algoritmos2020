def main():
	N = int(input())
	contador = 1
	M1 = 0
	M2 = 0
	while contador <= N:
		M1 = contador * contador
		M2 = contador * M1
		print(contador, end=' ')
		print(M1, end=' ')
		print(M2)
		print(contador, end=' ')
		print(M1+1, end=' ')
		print(M2+1)
		contador = contador + 1

main()