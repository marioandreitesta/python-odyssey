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
        if lista != limite_comprimentos:
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
    if a == b == c:
        equilatero: list[float] = comprimentos
    elif a == b and c != a and b:
        print("")