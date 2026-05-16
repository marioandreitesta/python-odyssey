"""Desevolva um programa que leia seis números inteiros e mostre a soma apenas daqueles
que forem pares. Se o valor digitado for ímpar, desconsidere-o."""


def receber_numeros() -> list[int]:
    div = 35
    print("=" * div)
    print("SOMA DE NÚMEROS PARES".center(div))
    print("=" * div)
    while True:
        entrada: str = input("Digite seus números inteiros\nseparados por espaço: ")
        print("-" * div)
        lista: list[str] = entrada.split()
        limite_num = 6
        if len(lista) != limite_num:
            print("-" * div)
            print(f"Você digitou {len(lista)}, é preciso seis números.")
            continue
        try:
            numeros: list[int] = list(map(int, lista))
            return numeros
        except ValueError:
            print("❌| Oops, isso não é um número.")


def processar_numeros(numeros: list[int]) -> None:
    soma_pares: int = 0
    for n in numeros:
        if n % 2 == 0:
            soma_pares += n
    print(f"A soma dos números \npares digitados é: {soma_pares}")


numeros: list[int] = receber_numeros()
processar_numeros(numeros)
