def main():
    # entrada
    a = int(input("Primeiro numero: "))
    b = int(input("Segundo numero: "))
    c = int(input("Terceiro numero: "))

    # processamento: Matemática + Condicionais + Repetições

    # saída
    print("Ordem crescente:")
    ordem_crescente(a,b,c)
    print()
    print("Ordem inicial:")
    print(a)
    print(b)
    print(c)
    

def ordem_crescente(n1,n2,n3):
	if n1 < n2 and n1 < n3:
		primeiro = n1
		if n2 < n3:
			segundo = n2
			terceiro = n3
		else:
			segundo = n3
			terceiro = n2

	if n2 < n1 and n2 < n3:
		primeiro = n2
		if n1 < n3:
			segundo = n1
			terceiro = n3
		else:
			segundo = n3
			terceiro = n1

	if n3 < n1 and n3 < n2:
		primeiro = n3
		if n2 < n1:
			segundo = n2
			terceiro = n1
		else:
			segundo = n1
			terceiro = n2

	print(primeiro)
	print(segundo)
	print(terceiro)


main()