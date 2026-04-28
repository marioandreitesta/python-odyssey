# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo. 

from math import radians, cos, sin, tan
from cores import LIMPAR, CINZA_BOLD, ROXO_BOLD, AMARELO_BOLD, AZUL_BOLD

DIV = 41

print(f"{CINZA_BOLD}={LIMPAR}"*DIV)
print(f"{CINZA_BOLD}CALCULADORA: {ROXO_BOLD}SENO, {AZUL_BOLD}COSSENO & {AMARELO_BOLD}TANGENTE{LIMPAR}".center(DIV))
print(f"{CINZA_BOLD}={LIMPAR}"*DIV)

angulo = float(input(f"{CINZA_BOLD}Digite o ângulo: {LIMPAR}"))
print(f"{CINZA_BOLD}-{LIMPAR}"*DIV)

print(f"{CINZA_BOLD}Calculando...".center(DIV))
print(f"{LIMPAR}{CINZA_BOLD}-{LIMPAR}"*DIV)

angulo_rad = radians(angulo)
seno = sin(angulo_rad)
cosseno = cos(angulo_rad)
tangente = tan(angulo_rad)

print(f"{ROXO_BOLD}->{CINZA_BOLD} SENO: {ROXO_BOLD}{seno:.2f}{LIMPAR}")
print(f"{AZUL_BOLD}->{CINZA_BOLD} COSSENO: {AZUL_BOLD}{cosseno:.2f}{LIMPAR}")
print(f"{AMARELO_BOLD}->{CINZA_BOLD} TANGENTE: {AMARELO_BOLD}{tangente:.2f}{LIMPAR}")