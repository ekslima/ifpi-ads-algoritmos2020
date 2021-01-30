def main():
	N = 0
	alcool = 0
	gasolina = 0
	diesel = 0

	while N != 4:
		N = int(input())
		
		if N == 1:
			alcool = alcool + 1
		elif N == 2:
			gasolina = gasolina + 1
		elif N == 3:
			diesel = diesel + 1

	print("MUITO OBRIGADO")
	print("Alcool: %d" % alcool)
	print("Gasolina: %d" % gasolina)
	print("Diesel: %d" % diesel)

main()