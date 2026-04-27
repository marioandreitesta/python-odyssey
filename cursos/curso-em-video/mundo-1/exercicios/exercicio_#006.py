# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

from cores import VERDE_BOLD, VERMELHO_BOLD, AZUL_BOLD, LIMPAR, CINZA_BOLD

print(f"Digite um número para ver seu {VERMELHO_BOLD}dobro, {VERDE_BOLD}triplo{LIMPAR} e {AZUL_BOLD}raiz quadrada.{LIMPAR}")

numero = int(input(f"{CINZA_BOLD}Digite o número: {LIMPAR}"))

dobro = numero * 2 
triplo = numero * 3
raiz_quadrada = numero ** 0.5

print(f"{CINZA_BOLD}Analisamos o número informado:{LIMPAR}")
print(f"Dobro: {VERMELHO_BOLD}{dobro}{LIMPAR}")
print(f"Triplo: {VERDE_BOLD}{triplo}{LIMPAR}")
print(f"Raiz quadrada: {AZUL_BOLD}{raiz_quadrada:.0f}{LIMPAR}")
