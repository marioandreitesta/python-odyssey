"""Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu
Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
IMC abaixo de 18,5: Abaixo do Peso
Entre 18,5 e 25: Peso ideal
25 até 30: Sobrepeso
30 até 40: Obesidade
Acima de 40: Obesidade Mórbida
"""

from enum import Enum


class StatusPesos(Enum):
    PESO_IDEAL = 25.0
    SOBREPESO = 30.0
    OBESIDADE = 40


def receber_peso() -> float:
    while True:
        try:
            peso = float(input("Informe seu peso: "))
            limite_peso_max = 600
            limite_peso_min = 0
            if peso > limite_peso_max or peso <= limite_peso_min:
                print("❌ | Digite um peso válido.")
            return peso
        except ValueError:
            print("❌ | Oops, isso não é um número!")


def receber_altura() -> float:
    while True:
        try:
            altura = float(input("Informe sua altura: "))
            altura_max = 2.50
            altura_min = 0.50
            if altura > altura_max or altura < altura_min:
                print("❌ | Digite um peso válido.")
            return altura
        except ValueError:
            print("❌ | Oops, isso não é um número!")


def processar_imc(peso: float, altura: float) -> None:
    imc: float = peso / (altura * altura)
    if imc <= StatusPesos.PESO_IDEAL.value:
        print(f"✅ | Seu IMC é {imc:.1f}, seu peso é ideal!")
    elif imc >= StatusPesos.SOBREPESO.value < StatusPesos.OBESIDADE.value:
        print(f"❕ | Seu IMC é {imc:.1f}, você está com sobrepeso!")
    elif imc == StatusPesos.OBESIDADE.value:
        print(f"❗ | Seu IMC é {imc:.1f}, você está obeso, procure um nutricionista.")
    elif imc > StatusPesos.OBESIDADE.value:
        print(
            f"‼ | Seu IMC é {imc:.1f}, você está com obesidade mórbida, procure ajuda médica imediatamente."
        )


peso: float = receber_peso()
altura: float = receber_altura()
processar_imc(peso, altura)
