"""Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de
triângulo será formado:
EQUILÁTERO: todos os lados iguais
ISÓCELES: dois lados iguais, um diferente
ESCALENO: todos os lados diferentes
"""


def receber_comprimentos() -> list[float]:
    while True:
        entrada: str = input("Digite três comprimentos separados por espaço: ")
        lista: list[str] = entrada.split()
        limite_comprimentos: int = 3
        if len(lista) != limite_comprimentos:
            print(f"❌ | Você digitou {len(lista)}, é preciso três números.")
        try:
            comprimentos: list[float] = list(map(float, lista))
            return comprimentos

        except ValueError:
            print("❌ | Use apenas números. Ex: 10, 12, 8.5")


def processar_comprimentos(comprimentos: list[float]) -> None:
    a: float = comprimentos[0]
    b: float = comprimentos[1]
    c: float = comprimentos[2]
    if a + b <= c or a + c <= b or b + c <= a:
        print("❌ | Estes comprimentos não podem formar um triângulo.")
    elif a == b == c:
        print(f"Estes comprimentos {comprimentos} formam um triângulo equilátero.")
    elif a in (b, c) or b == c:
        print(f"Estes comprimentos {comprimentos} formam um triângulo isóceles.")
    else:
        print(f"Estes comprimentos {comprimentos} formam um triângulo escaleno.")

comprimentos: list[float] = receber_comprimentos()
processar_comprimentos(comprimentos)
