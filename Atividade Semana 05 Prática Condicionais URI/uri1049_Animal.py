def main():
    # entrada
    n1 = input()
    n2 = input()
    n3 = input()

    # processamento: Matemática + Condicionais + Repetições

    # saída
    nome_do_animal(n1, n2, n3)
    

def nome_do_animal(n1,n2,n3):
	if n1 == "vertebrado" and n2 == "ave" and n3 == "carnivoro":
		print("Animal correspondente: aguia")
	elif n1 == "vertebrado" and n2 == "ave" and n3 == "onivoro":
		print("Animal correspondente: pomba")
	elif n1 == "vertebrado" and n2 == "mamifero" and n3 == "onivoro":
		print("Animal correspondente: homem")
	elif n1 == "vertebrado" and n2 == "mamifero" and n3 == "herbivoro":
		print("Animal correspondente: vaca")
	elif n1 == "invertebrado" and n2 == "inseto" and n3 == "hematofago":
		print("Animal correspondente: pulga")
	elif n1 == "invertebrado" and n2 == "inseto" and n3 == "herbivoro":
		print("Animal correspondente: lagarta")
	elif n1 == "invertebrado" and n2 == "anelideo" and n3 == "hematofago":
		print("Animal correspondente: sanguessuga")
	elif n1 == "invertebrado" and n2 == "anelideo" and n3 == "onivoro":
		print("Animal correspondente: minhoca")


main()