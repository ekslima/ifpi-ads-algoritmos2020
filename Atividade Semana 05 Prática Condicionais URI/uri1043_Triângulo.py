def main():
    # entrada
    a = float(input("Primeiro numero: "))
    b = float(input("Segundo numero: "))
    c = float(input("Terceiro numero: "))

    # processamento: Matemática + Condicionais + Repetições

    # saída
    forma_triangulo(a, b, c)
    

def forma_triangulo(num1,num2,num3):
	if num1 < (num2 + num3) and num2 < (num1 + num3) and num3 < (num1 + num2):
		perimetro_triangulo(num1,num2,num3)
	else:
		area_trapezio(num1,num2,num3)


def perimetro_triangulo(num1,num2,num3):
	soma = num1 + num2 + num3
	print("Perimetro = %.1f" % soma)


def area_trapezio(num1,num2,num3):
	area = ((num1 + num2) / 2) * num3
	print("Area = %.1f" % area)


main()