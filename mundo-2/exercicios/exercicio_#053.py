"""Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços"""

from time import sleep

from rich.align import Align
from rich.console import Console

console = Console()

DIV = 40


def receber_frase() -> str:
    console.print(Align.center("=" * DIV, style="bright_black"))
    console.print(Align.center("DETECTOR DE PALÍNDROMOS", style="bold green"))
    console.print(Align.center("=" * DIV, style="bright_black"))
    while True:
        console.print(Align.center(" ", style="s"))
        console.print("Digite uma frase qualquer: ", style="bold white", end=" ")
        entrada: str = input().strip()
        console.print(Align.center(" ", style="s"))
        frase_formatada: str = entrada.replace(" ", "").upper()
        if not frase_formatada.isalpha():
            console.print("❌ | Digite apenas letras e espaços.", style="red bold")
            continue
        return frase_formatada


def verificar_frase(frase_formatada: str) -> bool:
    with console.status("Verificando frase...", spinner="arc"):
        sleep(2)
    limite_frase: int = 50
    if len(frase_formatada) > limite_frase:
        console.print("❌ | Essa frase excede o limite de 50 letras.", style="bold red")
        return False
    return True


def processar_frase(frase_formatada: str) -> None:
    palindromo = True
    frase_invertida: str = frase_formatada[::-1]
    console.print(
        f"📄 | O inverso de {frase_formatada} é: {frase_invertida}", style="bold white"
    )
    console.print(Align.center(" ", style="s"))
    for indice in range(len(frase_formatada)):
        if frase_formatada[indice] != frase_invertida[indice]:
            palindromo = False
            break
    if palindromo:
        console.print("✔️ A frase digitada é um palíndromo!", style="bright_green")
    else:
        console.print("✖️ A frase digitada não é um palíndromo.", style="bright_red")


frase_formatada: str = receber_frase()
verificar: bool = verificar_frase(frase_formatada)
if verificar:
    verificar_frase(frase_formatada)
processar_frase(frase_formatada)
