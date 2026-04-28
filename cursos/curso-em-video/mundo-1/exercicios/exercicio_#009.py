# Crie um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

from cores import LIMPAR, CINZA_BOLD, AMARELO_UNDERLINE


print(f"{AMARELO_UNDERLINE}Gerador de Tabuada{LIMPAR}")
num = int(input(f"{AMARELO_UNDERLINE}Digite um número para ver a sua tabuada: "))

print(f"{LIMPAR}-" * 45)
print(f"{CINZA_BOLD}{num} x 1 = {num * 1}")
print(f"{num} x 2 = {num * 2}")
print(f"{num} x 3 = {num * 3}")
print(f"{num} x 4 = {num * 4}")
print(f"{num} x 5 = {num * 5}")
print(f"{num} x 6 = {num * 6}")
print(f"{num} x 7 = {num * 7}")
print(f"{num} x 8 = {num * 8}")
print(f"{num} x 9 = {num * 9}")
print(f"{num} x 10 = {num * 10}{LIMPAR}")
print("-" * 45)