# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quatidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados. 

from cores import ROXO_BACKGROUND, LIMPAR, CINZA_BOLD, ROXO_BOLD

print(f"{ROXO_BACKGROUND}Vamos começar a calcular a área de sua parede!{LIMPAR}")

altura_parede = float(input(f"{CINZA_BOLD}Digite a altura de sua parede: "))
largura_parede = float(input("Digite a largura de sua parede: "))

print(f"{LIMPAR}{ROXO_BOLD}Calculando área...{LIMPAR}")

area_parede = largura_parede * altura_parede

print(f"{CINZA_BOLD}A área de sua parede é{LIMPAR} {ROXO_BOLD}{area_parede:.1f}m²{LIMPAR}")

print(f"{ROXO_BACKGROUND}Agora vamos calcular o rendimento da tinta!{LIMPAR}")

rendimento_tinta = area_parede / 2

print(f"{CINZA_BOLD}Vai ser necessário {ROXO_BOLD}{rendimento_tinta:.1f}{LIMPAR} {CINZA_BOLD}litros de tinta para cobrir toda a área.{LIMPAR}")