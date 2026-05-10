"""Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
Média abaixo de 5.0: REPROVADO
Média entre 5.0 e 6.9: RECUPERAÇÃO
Média 7.0 ou superior: APROVADO"""

NOTA_MIN = 0.5
NOTA_MAX = 10.0


def receber_nota(mensagem: str) -> float:
    while True:
        try:
            nota = float(input(mensagem))
            if nota < NOTA_MIN or nota > NOTA_MAX:
                print("❌| A nota deve ser entre 0 e 10.")
                continue
            return nota
        except ValueError:
            print("❌| Apenas números são permitidos.")

def calcular_media() -> None:

    media_nota: float = (primeira_nota + segunda_nota) / 2
    nota_minima: float = 5.0
    nota_aprovacao: float = 7.0

    if media_nota < nota_minima:
        print(f"❌| Você foi reprovado, sua média foi: {media_nota}")
    elif nota_minima <= media_nota < nota_aprovacao:
        print(f"❗ | Sua média é {media_nota}, você está de recuperação, vá estudar!")
    else:
        print(f"✔️ | Parabéns, você foi aprovado!\n Sua média é: {media_nota}")


primeira_nota: float = receber_nota("Digite a primeira nota: ")
segunda_nota: float = receber_nota("Digite a segunda nota: ")

calcular_media()
