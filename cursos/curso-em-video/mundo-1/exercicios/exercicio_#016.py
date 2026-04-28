# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela sua porção inteira. 
# Ex: Digite um número: 6.127
# O número 6.127 tem a parte inteira 6. 

from math import trunc
from cores import LIMPAR, AZUL_BOLD, AZUL_BACKGROUND, CINZA_BOLD, VERDE_UNDERLINE

print(f"{AZUL_BOLD}={LIMPAR}"*40)
print(f"{AZUL_BACKGROUND}{'CONSULTE A PORÇÃO INTEIRA DE UM NÚMERO':^40}{LIMPAR}")
print(f"{AZUL_BOLD}={LIMPAR}"*40)

numero = float(input(f"{CINZA_BOLD}Digite um número:{LIMPAR} {VERDE_UNDERLINE}"))
print(f"{AZUL_BOLD}={LIMPAR}"*40)

porcao_int = trunc(numero)

print(f"{CINZA_BOLD}Porção inteira do número é: {VERDE_UNDERLINE}{porcao_int}{LIMPAR}")