# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo. 

from math import radians, cos, sin, tan

DIV = 50

print("="*DIV)
print("CALCULADORA: SENO, COSSENO & TANGENTE".center(DIV))
print("="*DIV)

angulo = float(input("Digite o ângulo: "))
print("-"*DIV)

print("Calculando...".center(DIV))
print("-"*DIV)

angulo_rad = radians(angulo)
seno = sin(angulo_rad)
cosseno = cos(angulo_rad)
tangente = tan(angulo_rad)

print(f"-> SENO: {seno:.2f}")
print(f"-> COSSENO: {cosseno:.2f}")
print(f"-> TANGENTE: {tangente:.2f}")