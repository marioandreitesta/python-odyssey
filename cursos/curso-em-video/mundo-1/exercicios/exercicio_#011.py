# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quatidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados. 

print("Vamos começar a calcular a área de sua parede!")

altura_parede = float(input("Digite a altura de sua parede: "))
largura_parede = float(input("Digite a largura de sua parede: "))

print("Calculando área...")

area_parede = largura_parede * altura_parede

print(f"A área de sua parede é {area_parede:.1f}m²")

print("Agora vamos calcular o rendimento da tinta!")

rendimento_tinta = area_parede / 2

print(f"Vai ser necessário {rendimento_tinta:.1f} litros de tinta para cobrir toda a área.")