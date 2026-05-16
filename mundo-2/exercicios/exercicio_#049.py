"""Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só
que agora utilizando um laço for"""


def base_tabuada() -> int:
    div = 60
    print("=" * div)
    print("TABUADA (MULTIPLICAÇÃO)".center(div))
    print("=" * div)
    while True:
        try:
            base = int(input("Digite o número desejado para ver sua tabuada: "))
            print("-" * div)
            limite = range(0, 101)
            if base not in limite:
                print("❌ | Digite um número válido.")
            else:
                return base
        except ValueError:
            print("❌ | Apenas números inteiros são permitidos.")


def processar_tabuada(base: int) -> None:
    for n in range(1, 11):
        tabuada: int = n * base
        print(f"{base} * {n}: {tabuada}")


base: int = base_tabuada()
processar_tabuada(base)
