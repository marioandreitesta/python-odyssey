# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo

from time import sleep

from rich.align import Align
from rich.console import Console

console = Console()


def receber_numero() -> int:
    console.print(Align.center(" ", style="s"))
    console.print(Align.center("VERIFICADOR DE NÚMEROS PRIMOS", style="bright_black"))
    console.print(Align.center(" ", style="s"))
    while True:
        try:
            limite = 1
            console.print("Digite um número inteiro: ", style="yellow", end=" ")
            numero = int(input())
            if numero >= limite:
                console.print(Align.center(" ", style="s"))
                with console.status("Processando número...", spinner="arc"):
                    sleep(2)
                return numero
            console.print("❌ | Esse número não é válido.", style="bold red")
        except ValueError:
            console.print("❌ | Apenas números são aceitos.", style="bold red")


def processar_numero(numero: int) -> int:
    contador = 0
    console.print("Resultado: ", end="", style="bold white")
    for divisor in range(1, numero + 1):
        if numero % divisor == 0:
            console.print(f"{divisor}", style="bold bright_green", end=" ")
            sleep(1)
            contador += 1
        else:
            console.print(f"{divisor}", style="bold bright_red", end=" ")
            sleep(1)
    print()
    return contador


def verificar_contador(numero: int, contador: int) -> None:
    numero_primo = 2
    if contador != numero_primo:
        console.print(
            Align.center(
                f"Esse número [{numero}] não é primo, pois é dividido {contador} vezes.",
                style="bold red",
            )
        )
    else:
        console.print(Align.center(f"O número [{numero}] é primo.", style="bold green"))


numero: int = receber_numero()
contador: int = processar_numero(numero)
verificar_contador(numero, contador)
