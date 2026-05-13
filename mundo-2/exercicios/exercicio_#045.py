# Crie um programa que faça o computador jogar Jokenpô com você.

from enum import Enum
from random import randrange


class OpcoesJogadas(Enum):
    PEDRA = 1
    PAPEL = 2
    TESOURA = 3


def escolha_usuario() -> int:
    div = 30
    print("=" * div)
    print("Vamos jogar Jokenpô!".center(div))
    print("=" * div)
    print("Escolha entre:\nPedra [1]\nPapel [2]\nTesoura [3]")
    while True:
        try:
            print("-" * div)
            jogada_usuario = int(input("Digite sua jogada: "))
            print("-" * div)
            if jogada_usuario not in [e.value for e in OpcoesJogadas]:
                print("❌| Escolha um número válido.")
            return jogada_usuario
        except ValueError:
            print("❌| Oops! Apenas números são permitidos.")


def escolha_computador() -> int:
    div = 30
    print("O computador está escolhendo...")
    print("-" * div)
    jogada_computador: int = randrange(1, 4)
    if jogada_computador == OpcoesJogadas.PEDRA.value:
        print(f"O computador escolheu: {OpcoesJogadas.PEDRA.name}")
    elif jogada_computador == OpcoesJogadas.PAPEL.value:
        print(f"O computador escolheu: {OpcoesJogadas.PAPEL.name}")
    else:
        print(f"O computador escolheu: {OpcoesJogadas.TESOURA.name}")
    print("-" * div)
    return jogada_computador


class Resultado(Enum):
    EMPATE = 0
    VENCEDOR = 1


def processar_jogadas(jogada_usuario: int, jogada_computador: int) -> None:
    diferenca: int = (jogada_usuario - jogada_computador) % 3
    if diferenca == Resultado.EMPATE.value:
        print("🤝| Empate!")
    elif diferenca == Resultado.VENCEDOR.value:
        print("🏆| Você venceu!")
    else:
        print("❌ | Você perdeu!")


jogada_usuario: int = escolha_usuario()
jogada_computador: int = escolha_computador()
processar_jogadas(jogada_usuario, jogada_computador)
