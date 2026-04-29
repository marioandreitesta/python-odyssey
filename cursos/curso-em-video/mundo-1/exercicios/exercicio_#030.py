# Faça um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

from cores import AMARELO_BOLD, ROXO_BOLD, CINZA_BOLD, LIMPAR

DIV = 27

print(f'{CINZA_BOLD}ESSE NÚMERO É {AMARELO_BOLD}PAR{CINZA_BOLD} OU {ROXO_BOLD}ÍMPAR{CINZA_BOLD}?')
print(f'{LIMPAR}{CINZA_BOLD}-{LIMPAR}' * DIV)

try:
    numero = int(input(f'{CINZA_BOLD}Digite um número: {LIMPAR}'))

    if numero % 2 == 0:
        print(f'{AMARELO_BOLD}Esse número é PAR!{LIMPAR}')
    else:
        print(f'{ROXO_BOLD}Esse número é ÍMPAR!{LIMPAR}')
except ValueError:
    print(f'{CINZA_BOLD}Isso não é um número, tente novamente!{LIMPAR}')

