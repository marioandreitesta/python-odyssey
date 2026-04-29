# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h mostre uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$7,00 por cada Km acima do limite. 

from random import randrange

DIV = 27
VELOCIDADE_CARRO = randrange(10, 220)
LIMITE_RADAR = 80
VALOR_MULTA = (VELOCIDADE_CARRO - LIMITE_RADAR) * 7

print('' * DIV)
print('RADAR DE VELOCIDADE 80KM/H')
print('-' * DIV)

if VELOCIDADE_CARRO > LIMITE_RADAR:
    print(f'Você ultrapassou o limite de velocidade! [{VELOCIDADE_CARRO}Km/h]')
    print(f'Multa: R${VALOR_MULTA:.2f}')
else:
    print('Tenha uma boa viagem!')