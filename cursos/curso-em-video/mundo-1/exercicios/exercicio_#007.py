# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

from cores import VERMELHO_BACKGROUND, VERMELHO_BOLD, LIMPAR, CINZA_BOLD

print(f"{VERMELHO_BACKGROUND}Digite a nota do aluno para saber sua média!{LIMPAR}")

primeiraNota = float(input(f"{VERMELHO_BOLD}Digite a primeira nota: "))
segundaNota = float(input("Digite a segunda nota: "))
resultado_soma = (primeiraNota + segundaNota) / 2

print(f"{LIMPAR}{CINZA_BOLD}Calculamos sua média:")
print(f"A média desse aluno é: {LIMPAR}{VERMELHO_BOLD}{resultado_soma:.1f}{LIMPAR}")