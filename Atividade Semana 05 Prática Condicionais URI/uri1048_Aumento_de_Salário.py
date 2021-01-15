def main():
    # entrada
    salario = float(input("Salario do funcionario: "))

    # processamento: Matemática + Condicionais + Repetições

    # saída
    novo_salario(salario)
    

def novo_salario(valor):
	if valor > 0 and valor <= 400.00:
		reajuste = valor * 0.15
		valor_final = valor + reajuste
		print("Novo salario: %.2f" % valor_final)
		print("Reajuste ganho: %.2f" % reajuste)
		print("Em percentual: 15 %")
	elif valor > 400.00 and valor <= 800.00:
		reajuste = valor * 0.12
		valor_final = valor + reajuste
		print("Novo salario: %.2f" % valor_final)
		print("Reajuste ganho: %.2f" % reajuste)
		print("Em percentual: 12 %")
	elif valor > 800.00 and valor <= 1200.00:
		reajuste = valor * 0.10
		valor_final = valor + reajuste
		print("Novo salario: %.2f" % valor_final)
		print("Reajuste ganho: %.2f" % reajuste)
		print("Em percentual: 10 %")
	elif valor > 1200.00 and valor <= 2000.00:
		reajuste = valor * 0.07
		valor_final = valor + reajuste
		print("Novo salario: %.2f" % valor_final)
		print("Reajuste ganho: %.2f" % reajuste)
		print("Em percentual: 7 %")
	elif valor > 2000.00:
		reajuste = valor * 0.04
		valor_final = valor + reajuste
		print("Novo salario: %.2f" % valor_final)
		print("Reajuste ganho: %.2f" % reajuste)
		print("Em percentual: 4 %")


main()