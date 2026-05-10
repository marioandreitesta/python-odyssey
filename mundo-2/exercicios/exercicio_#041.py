"""A Confederação Nacional de Natação precisa de um programa que leia o ano de
nascimento de um atleta e mostre sua categoria, de acordo com a idade:
Até 9 anos: MIRIM
Até 14 anos: INFANTIL
Até 19 anos: JUNIOR
Até 25 anos: SÊNIOR
Acima de 25 anos: MASTER
"""

from enum import Enum

ANO_ATUAL: int = 2026


class CategoriaAtleta(Enum):
    MIRIM = 9
    INFANTIL = 14
    JUNIOR = 19
    SENIOR = 25


def receber_ano_nascimento() -> int:
    while True:
        try:
            limite_ano_nasc: int = ANO_ATUAL - 100
            ano_nascimento = int(input("Informe seu ano de nascimento: "))
            if ano_nascimento < limite_ano_nasc or ano_nascimento >= ANO_ATUAL:
                print("❌ | Informe um ano de nascimento válido!")
                continue
            return ano_nascimento
        except ValueError:
            print("❌ | Apenas números são permitidos!")


def processar_categorias(ano_nascimento: int) -> None:
    idade_atleta: int = ANO_ATUAL - ano_nascimento
    if CategoriaAtleta.MIRIM.value <= idade_atleta < CategoriaAtleta.INFANTIL.value:
        print(f"✔️ | Cadastro Realizado!\n📋| Categoria: {CategoriaAtleta.MIRIM.name}")
    elif CategoriaAtleta.INFANTIL.value <= idade_atleta < CategoriaAtleta.JUNIOR.value:
        print(
            f"✔️ | Cadastro Realizado!\n📋| Categoria: {CategoriaAtleta.INFANTIL.name}"
        )
    elif CategoriaAtleta.JUNIOR.value <= idade_atleta < CategoriaAtleta.SENIOR.value:
        print(f"✔️ | Cadastro Realizado!\n📋| Categoria: {CategoriaAtleta.SENIOR.name}")
    elif idade_atleta > CategoriaAtleta.SENIOR.value:
        print("✔️ | Cadastro Realizado!\n📋| Categoria: MASTER")
    else:
        print("❌ | Você não tem idade necessária para se inscrever ainda.")


ano_nascimento: int = receber_ano_nascimento()
processar_categorias(ano_nascimento)
