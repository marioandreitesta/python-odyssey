# O mesmo professor do desafio #019 quer sortear a ordem de apresentação de trabalho dos alunos. 
# Faça um programa que leia o nome dos alunos e mostre a ordem sorteada.

from random import shuffle
from cores import AZUL_BOLD, LIMPAR, CINZA_BOLD, VERDE_BOLD, AMARELO_BOLD, VERMELHO_BOLD

DIV = 45

print(f"{AZUL_BOLD}={LIMPAR}"*DIV)
print("LISTA DE APRESENTAÇÃO DOS ALUNOS".center(DIV))
print(f"{AZUL_BOLD}={LIMPAR}"*DIV)

aluno0 = input(f"{CINZA_BOLD}Digite o nome do {VERDE_BOLD}1° {CINZA_BOLD}aluno: {LIMPAR}")
aluno1 = input(f"{CINZA_BOLD}Digite o nome do {AZUL_BOLD}2° {CINZA_BOLD}aluno: {LIMPAR}")
aluno2 = input(f"{CINZA_BOLD}Digite o nome do {AMARELO_BOLD}3° {CINZA_BOLD}aluno: {LIMPAR}")
aluno3 = input(f"{CINZA_BOLD}Digite o nome do {VERMELHO_BOLD}4° {CINZA_BOLD}aluno: {LIMPAR}")
print(f"{LIMPAR}{AZUL_BOLD}-{LIMPAR}"*DIV)

alunos = [aluno0, aluno1, aluno2, aluno3]
ordem_alunos = shuffle(alunos)

print("ORDEM DE APRESENTAÇÃO:".center(DIV))
print(f"{AZUL_BOLD}-{LIMPAR}"*DIV)
print(f"{VERDE_BOLD}1° {CINZA_BOLD}Lugar: {VERDE_BOLD}{alunos[0]}{LIMPAR}")
print(f"{AZUL_BOLD}2° {CINZA_BOLD}Lugar: {AZUL_BOLD}{alunos[1]}{LIMPAR}")
print(f"{AMARELO_BOLD}3° {CINZA_BOLD}Lugar: {AMARELO_BOLD}{alunos[2]}{LIMPAR}")
print(f"{VERMELHO_BOLD}4° {CINZA_BOLD}Lugar: {VERMELHO_BOLD}{alunos[3]}{LIMPAR}")