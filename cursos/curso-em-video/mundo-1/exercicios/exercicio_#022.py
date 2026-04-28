# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúsculas;
# Quantas letras ao todo (sem considerar espaços);
# Quantas letras tem o primeiro nome.

from cores import LIMPAR, ROXO_BOLD, CINZA_BOLD

DIV = 44

print('' * DIV)
print(f'{ROXO_BOLD}CURIOSIDADES SOBRE O SEU NOME{LIMPAR}'.center(DIV))
print('' * DIV)

nome = input(f'{CINZA_BOLD}Digite seu nome completo: {ROXO_BOLD}').strip()
print(f'{LIMPAR}-' * DIV)

nome_dividido = nome.split()

print(f'{CINZA_BOLD}Seu nome em maiúsculo: {ROXO_BOLD}{nome.upper()}')
print(f'{CINZA_BOLD}Seu nome em minúsculo: {ROXO_BOLD}{nome.lower()}')
print(f'{CINZA_BOLD}Quantidade de letras em seu nome completo: {ROXO_BOLD}{len(nome)}')
print(f'{CINZA_BOLD}Quantidade de letras em seu primeiro nome: {ROXO_BOLD}{len(nome_dividido[0])}{LIMPAR}')
