# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

from cores import ROXO_BOLD, CINZA_BOLD, LIMPAR, VERDE_BOLD, VERMELHO_BOLD

nome_cidade = input(f'{ROXO_BOLD}Digite o nome da sua cidade: {CINZA_BOLD}').strip()

nome_cidade = nome_cidade.upper()

if nome_cidade.startswith('SANTO'):
    print(f'{CINZA_BOLD}O nome da cidade digitado começa com "{VERDE_BOLD}Santo"')
else:
    print(f'{CINZA_BOLD}O nome da sua cidade não começa com "{VERMELHO_BOLD}Santo{LIMPAR}"')

