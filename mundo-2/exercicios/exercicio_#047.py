"""Crie um programa que mostre na tela todos os números pares que estão no intervalo
entre 1 e 50"""

from time import sleep


def contar_pares() -> None:
    for n in range(2, 51, 2):
        print(n)
        sleep(1)


contar_pares()
