"""Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final,
mostre os 10 primeiros termos dessa progressão."""


def primeiro_termo() -> int:
    div = 30
    print("=" * div)
    print("PROGRESSÃO ARITMÉTICA (P.A)".center(div))
    print("=" * div)
    while True:
        try:
            return int(input("Digite o primeiro termo: "))
        except ValueError:
            print("❌| Apenas números inteiros são permitidos.")


def razao() -> int:
    while True:
        try:
            return int(input("Digite a razão da P.A: "))
        except ValueError:
            print("❌| Apenas números inteiros são permitidos.")


def progressao_aritmetica(primeiro_termo: int, razao: int) -> None:
    termo: int = primeiro_termo
    for i in range(1, 11):
        print(f"{i}° termo: {termo}")
        termo += razao


progressao_aritmetica(primeiro_termo(), razao())
