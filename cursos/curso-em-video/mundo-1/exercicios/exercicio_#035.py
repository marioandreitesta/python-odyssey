# Desenvolva um programa que leia três retas e diga ao usuário se elas podem ou não formar um triângulo. 

import cores

def receber_comprimento():

    while True:
        entrada = input(f"\n {cores.AMARELO_BOLD}Digite três comprimentos separados por espaço: {cores.LIMPAR}")
        lista = entrada.split()

        if len(lista) != 3:
            print(f"{cores.CINZA_BOLD}Você digitou {cores.VERMELHO_BOLD}{len(lista)}{cores.CINZA_BOLD}, é preciso de exatamente {cores.VERDE_BOLD}três.{cores.LIMPAR}")
            continue

        try:
            comprimentos = list(map(float, lista))
            return comprimentos
        
        except ValueError:
            print(f"{cores.VERMELHO_BOLD}Error{cores.CINZA_BOLD}: Use apenas números. Ex: {cores.AMARELO_BOLD}20 12 3.7{cores.LIMPAR}")

def calcular_triangulo(comprimentos):

    a = comprimentos[0]
    b = comprimentos[1]
    c = comprimentos[2]

    if a + b > c and a + c > b and b + c > a: # Condição de Existência de um Triângulo
        print(f"{cores.CINZA_BOLD}Os comprimentos informados {cores.VERDE_BOLD}podem{cores.CINZA_BOLD} formar um triângulo!{cores.LIMPAR}")
    else:
        print(f"{cores.CINZA_BOLD}Os comprimentos informados {cores.VERMELHO_BOLD}{comprimentos} não {cores.CINZA_BOLD}podem formar um triângulo.{cores.LIMPAR}")

comprimentos = receber_comprimento()
calcular_triangulo(comprimentos)
