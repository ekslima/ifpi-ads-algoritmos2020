def main():
    # entrada
    hora_inicial = float(input("Horário inicial: "))
    hora_final = float(input("Horário final: "))

    # processamento: Matemática + Condicionais + Repetições

    # saída
    duracao_do_jogo(hora_inicial, hora_final)
    

def duracao_do_jogo(inicio,fim):
	if inicio > fim:
		duracao = (fim + 24) - inicio
		print('O JOGO DUROU %d HORA(S)' % duracao)
	elif inicio < fim:
		duracao = fim - inicio
		print('O JOGO DUROU %d HORA(S)' % duracao)
	else:
		print('O JOGO DUROU 24 HORA(S)')


main()