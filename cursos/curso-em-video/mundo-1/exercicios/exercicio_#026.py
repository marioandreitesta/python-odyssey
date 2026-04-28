# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez. 

from cores import LIMPAR, CINZA_BOLD, CIANO_UNDERLINE, CIANO_BOLD

DIV = 40

frase = input(f'{CINZA_BOLD}Digite uma frase: {CIANO_BOLD}').strip()
print(f'{LIMPAR}' * DIV)

frase_formatada = frase.lower()
contando_a = frase.count('a')

print(f'{CINZA_BOLD}Quantas vezes a palavra {CIANO_BOLD}"A" {CINZA_BOLD}aparece na frase: {CIANO_UNDERLINE}{contando_a}{LIMPAR}')
print(f'{CINZA_BOLD}Posição da primeira aparição: {CIANO_UNDERLINE}{frase_formatada.find('a')}')
print(f'{LIMPAR}{CINZA_BOLD}Posição da última aparição: {CIANO_BOLD}{frase_formatada.rfind('a')}{LIMPAR}')