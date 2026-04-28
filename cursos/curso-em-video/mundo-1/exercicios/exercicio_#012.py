# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

from cores import CINZA_BOLD
from cores import AMARELO_BOLD, AMARELO_BACKGROUND, LIMPAR, VERMELHO_BOLD, VERDE_BOLD

print(f"{AMARELO_BACKGROUND}Calculador de Descontos!{LIMPAR}")

preco_produto = float(input(f"{CINZA_BOLD}Digite o preço do seu produto: {AMARELO_BOLD}R$"))

preco_final = preco_produto * 0.95
desconto = preco_final - preco_produto

print(f"{LIMPAR}{CINZA_BOLD}-{LIMPAR}" * 40)

print(f"{CINZA_BOLD}Preço do produto: {AMARELO_BOLD}R${preco_produto:.2f}")
print(f"{CINZA_BOLD}Desconto (5%): {VERMELHO_BOLD}R${desconto:.2f}")
print(f"{CINZA_BOLD}Valor final: {VERDE_BOLD}R${preco_final:.2f}{LIMPAR}")