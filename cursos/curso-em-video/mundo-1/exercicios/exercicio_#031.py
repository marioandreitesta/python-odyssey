# Desenvolva um programa que pergunte a distância de uma viagem em Km. 
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas. 

import cores

DIV = 29
CUSTO_KM = 0.50
CUSTO_KM_PROMO = 0.45

print(f'{cores.CINZA_BOLD}CALCULE O CUSTO DE SUA VIAGEM{cores.LIMPAR}')
print(f'{cores.CINZA_BOLD}-{cores.LIMPAR}' * DIV)

try:
    distancia = float(input(f'{cores.CINZA_BOLD}Digite a distância {cores.AMARELO_BOLD}[Km]{cores.CINZA_BOLD}: '))

    if distancia <= 200:
        custo_viagem = distancia * CUSTO_KM
        print(f'{cores.LIMPAR}{cores.CINZA_BOLD}O custo da sua viagem é: {cores.VERDE_BOLD}R${cores.CINZA_BOLD}{custo_viagem:.2f}{cores.LIMPAR}')
    else:
        custo_viagem = distancia * CUSTO_KM_PROMO
        print(f'{cores.CINZA_BOLD}O custo da sua viagem é: {cores.VERDE_BOLD}R${cores.CINZA_BOLD}{custo_viagem:.2f}{cores.LIMPAR}')
except ValueError:
    print(f'{cores.VERMELHO_BOLD}Error{cores.CINZA_BOLD}: isso não é um número!{cores.LIMPAR}')
