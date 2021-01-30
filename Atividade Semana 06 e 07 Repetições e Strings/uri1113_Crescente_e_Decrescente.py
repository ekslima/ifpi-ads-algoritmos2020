def main():
	while True:
        linha = input()
        dados = linha.split()
        X = int(dados[0])
        Y = int(dados[1])
		if X > Y:
			print("Decrescente")
		elif X < Y:
			print("Crescente")
		else:
			break

main()