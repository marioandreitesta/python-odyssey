"""Faça um programa que calcule a soma entre todos os números que são multiplos de três
e que se encontram no intervalo de 1 até 500."""


def contar_multiplos() -> None:
    div = 30
    print("=" * div)
    print("Números Multiplos de Três:".center(div))
    print("=" * div)
    soma: int = 0
    soma = sum(range(3, 501, 3))
    print(f"A soma dos múltiplos\nde 3 de 1 até 500 é: {soma}")


contar_multiplos()
