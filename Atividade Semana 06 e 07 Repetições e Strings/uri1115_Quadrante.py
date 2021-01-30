def main():	
	while True:
        linha = input()
        dados = linha.split()
        X = int(dados[0])
        Y = int(dados[1])
		if X == 0 or Y == 0:
			break
		elif X > 0 and Y > 0:
			print("primeiro")
		elif X < 0 and Y > 0:
			print("segundo")
		elif X < 0 and Y < 0:
			print("terceiro")
		else:
			print("quarto")
main()