# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 centavos por Km rodado. 

import cores
    
print(f"{cores.CINZA_BOLD}Calculadora de Gastos {cores.AMARELO_BOLD}(Aluguel de Carros){cores.LIMPAR}")

dias_alugados = int(input(f"{cores.CINZA_BOLD}Para começar, informe quantos {cores.AMARELO_BOLD}dias{cores.CINZA_BOLD} você alugou o carro: {cores.AMARELO_UNDERLINE}"))
km_percorridos = float(input(f"{cores.LIMPAR}{cores.CINZA_BOLD}Agora, digite quantos {cores.AMARELO_BOLD}quilômetros{cores.CINZA_BOLD} você percorreu: {cores.AMARELO_UNDERLINE}"))

print(f"{cores.LIMPAR}{cores.BRANCO_BACKGROUND}Estamos calculando o seu gasto...{cores.LIMPAR}")
print(f"{cores.AMARELO_BOLD}-{cores.LIMPAR}" * 40)

PRECO_DIARIA = 60
PRECO_KM = 0.15

custo_aluguel = dias_alugados * PRECO_DIARIA
custo_quilometragem = km_percorridos * PRECO_KM
custo_total = custo_aluguel + custo_quilometragem

print(f"{cores.CINZA_BOLD}Você alugou o carro por {cores.AMARELO_BOLD}{dias_alugados}{cores.CINZA_BOLD} dias, pelo valor de {cores.VERDE_BOLD}R${cores.CINZA_BOLD}{custo_aluguel:.2f}{cores.LIMPAR}")
print(f"{cores.CINZA_BOLD}O custo do aluguel é: {cores.VERDE_BOLD}R${cores.LIMPAR}{cores.CINZA_BOLD}{custo_aluguel:.2f}{cores.LIMPAR}")
print(f"{cores.CINZA_BOLD}O custo por quilômetros rodados é: {cores.VERDE_BOLD}R${cores.LIMPAR}{cores.CINZA_BOLD}{custo_quilometragem:.2f}{cores.LIMPAR}")
print(f"{cores.AMARELO_BOLD}Custo final: {cores.VERDE_BOLD}R${cores.LIMPAR}{cores.CINZA_BOLD}{custo_total:.2f}{cores.LIMPAR}")

