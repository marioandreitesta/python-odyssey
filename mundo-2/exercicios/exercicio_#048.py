"""Faça um programa que calcule a soma entre todos os números que são multiplos de três
e que se encontram no intervalo de 1 até 500."""

from time import sleep


def contar_multiplos() -> None:
    div = 30
    print("Números Multiplos de Três:".center(div))
    print("=" * div)
    soma: int = 0
    for i in range(3, 501, 3):
        sleep(0.02)
        soma += i
        print(i)
    print(f"A soma dos múltiplos de 3 de 1 até 500 é: {soma}")


contar_multiplos()
