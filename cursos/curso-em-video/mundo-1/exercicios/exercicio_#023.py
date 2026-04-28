# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.

from cores import LIMPAR, AMARELO_BOLD, CINZA_BOLD

DIV = 30

print('' * DIV)
print(f'{AMARELO_BOLD}SEPARANDO DIGITOS DE UM NÚMERO{LIMPAR}'.center(DIV))
print(f'{CINZA_BOLD}={LIMPAR}' * DIV)

numero = int(input(f'{CINZA_BOLD}Digite um número: {AMARELO_BOLD}'))
print(f'{CINZA_BOLD}-{LIMPAR}' * DIV)

unidade = numero % 10
dezena = (numero // 10) % 10
centena = (numero // 100) % 10
milhar = (numero // 1000) % 10

print(f'{CINZA_BOLD}Unidade: {AMARELO_BOLD}{unidade}')
print(f'{CINZA_BOLD}Dezena: {AMARELO_BOLD}{dezena}')
print(f'{CINZA_BOLD}Centena: {AMARELO_BOLD}{centena}')
print(f'{CINZA_BOLD}Milhar: {AMARELO_BOLD}{milhar}{LIMPAR}')