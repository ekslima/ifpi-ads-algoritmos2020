def main():
    # entrada
    a = float(input("Primeiro numero: "))
    b = float(input("Segundo numero: "))

    # processamento: Matemática + Condicionais + Repetições

    # saída
    se_sao_multiplos(a, b)
    

def se_sao_multiplos(num1,num2):
	if num1 % num2 == 0 or num2 % num1 == 0:
		print("Sao Multiplos")
	else:
		print("Nao sao Multiplos")


main()