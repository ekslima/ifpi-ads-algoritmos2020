def main():
    N = int(input())

    contador = 1
    total = 0
    total_coelhos = 0
    total_ratos = 0
    total_sapos = 0

    while contador <= N:
	    Quantia = input()
	    partes = Quantia.split()
	    cobaias = int(partes[0])
	    tipo = str(partes[1])
	    if tipo == 'C':
	    	total_coelhos = total_coelhos + cobaias
	    elif tipo == 'R':
	    	total_ratos = total_ratos + cobaias
	    elif tipo == 'S':
	    	total_sapos = total_sapos + cobaias
	    contador = contador + 1

    total = total_coelhos + total_ratos + total_sapos
    percentual_coelhos = (total_coelhos * 100) / total
    percentual_ratos = (total_ratos * 100) / total
    percentual_sapos = (total_sapos * 100) / total

    print('Total: %d cobaias' % total)
    print('Total de coelhos:', total_coelhos)
    print('Total de ratos:', total_ratos)
    print('Total de sapos:', total_sapos)
    print('Percentual de coelhos: %.2f %%' % percentual_coelhos)
    print('Percentual de ratos: %.2f %%' % percentual_ratos)
    print('Percentual de sapos: %.2f %%' % percentual_sapos)

main()