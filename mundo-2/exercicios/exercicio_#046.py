"""Faça um programa que mostre na tela uma contagem regressiva para o estouro de
fogos de artíficio, indo de 10 até 0, com uma pausa de 1 segundo entre eles."""

from time import sleep

DIV = 60


def iniciar_contagem() -> bool:
    print("=" * DIV)
    print("✨Show de Fogos de Artíficio!✨".center(DIV))
    print("=" * DIV)
    while True:
        entrada: str = (
            input("Deseja inicar a contagem dos fogos? [Sim/Não] ").strip().lower()
        )
        if entrada == "sim":
            print("-" * DIV)
            print("Iniciando contagem!".center(DIV))
            print("-" * DIV)
            return True
        if entrada in {"não", "nao"}:
            print("-" * DIV)
            print("Não me faça insistir: digite [Sim]!".center(DIV))
            print("-" * DIV)
        else:
            print("❌ | Responda com apenas [Sim] ou [Não]")


def processar_contagem() -> None:
    for num in range(10, -1, -1):
        print(num)
        sleep(1)
    print("🥳🎉✨ BOOOOM! ✨🎉🥳")


if iniciar_contagem():
    processar_contagem()
