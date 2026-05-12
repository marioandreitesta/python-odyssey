"""Elabora um programa que calcule o valor a ser pago por um produto, considerando
o seu preço normal e condição de pagamento:
à vista dinheiro/cheque: 10% de desconto
à vista no cartão: 5% de desconto
em até 2x no cartão: preço formal
3x ou mais no cartão: 20% de juros
"""

from enum import Enum


def receber_valor_produto() -> float:
    while True:
        try:
            preco_produto: float = float(input("Digite o preço do produto: R$"))
            preco_min: float = 0
            if preco_produto <= preco_min:
                print("❌| Digite um valor válido")
                continue
            return preco_produto
        except ValueError:
            print("❌| Apenas números são permitidos.")


def selecionar_formas_de_pagamento() -> int:
    div = 45
    print("=" * div)
    print("Formas de Pagamento".center(div))
    print("=" * div)
    print("💵| Dinheiro/Cheque | 10% de desconto: [1]")
    print("💳| À vista no cartão | 5% de desconto: [2]")
    print("💳| Parcelado em 2x: [3]")
    print("💳| 3x ou mais no cartão | 20% de juros: [4]")
    num_formas_pagamentos = (1, 2, 3, 4)
    while True:
        try:
            forma_de_pagamento = int(input("Escolha a forma de pagamento: "))
            if forma_de_pagamento not in num_formas_pagamentos:
                print("❌| Escolha uma forma de pagamento válida!")
            return forma_de_pagamento
        except ValueError:
            print("❌| Oops, isso não é um número.")


class FormaPagamento(Enum):
    DINHEIRO_CHEQUE = 1
    A_VISTA_CARTAO = 2
    CARTAO_PARCELADO_2X = 3
    CARTAO_PARCELADO_3X = 4


class Descontos(Enum):
    DINHEIRO_CHEQUE = 0.90
    CARTAO_A_VISTA = 0.95
    CARTAO_PARCELADO_2X = 1.00
    CARTAO_PARCELADO_3X = 1.20


def calcular_desconto(
    preco_produto: float, forma_de_pagamento: int
) -> tuple[float, float, str, str, float]:
    if forma_de_pagamento == FormaPagamento.DINHEIRO_CHEQUE.value:
        preco_final = preco_produto * Descontos.DINHEIRO_CHEQUE.value
        exibir_forma_pagamento = "Dinheiro/Cheque"
        exibir_desconto = "Desconto [10%]:"
    elif forma_de_pagamento == FormaPagamento.A_VISTA_CARTAO.value:
        preco_final = preco_produto * Descontos.CARTAO_A_VISTA.value
        exibir_forma_pagamento = "À Vista no Cartão"
        exibir_desconto = "Desconto [5%]:"
    elif forma_de_pagamento == FormaPagamento.CARTAO_PARCELADO_3X.value:
        preco_final = preco_produto * Descontos.CARTAO_PARCELADO_3X.value
        exibir_forma_pagamento = "Cartão [3x ou mais]"
        exibir_desconto = "Juros [20%]:"
    elif forma_de_pagamento == FormaPagamento.CARTAO_PARCELADO_2X.value:
        preco_final = preco_produto * Descontos.CARTAO_PARCELADO_2X.value
        exibir_forma_pagamento = "Cartão [2x Parcelas]"
        exibir_desconto = "Sem acréscimo:"

    valor_desconto: float = preco_produto - preco_final
    return (
        preco_produto,
        preco_final,
        exibir_forma_pagamento,
        exibir_desconto,
        valor_desconto,
    )


def exibir_resultado(
    preco_produto: float,
    exibir_forma_pagamento: str,
    exibir_desconto: str,
    preco_final: float,
    valor_desconto: float,
) -> None:

    div = 45
    print("=" * div)
    print("RESUMO DO PEDIDO".center(div))
    print("=" * div)
    print(f"Preço do produto: R${preco_produto:.2f}")
    print(f"Forma de pagamento: {exibir_forma_pagamento}")
    if valor_desconto < 0:
        print(f"{exibir_desconto} R${abs(valor_desconto):.2f}")
    else:
        print(f"{exibir_desconto} -R${valor_desconto:.2f}")
    print(f"Preco final: R${preco_final:.2f}")
    print("=" * div)


preco_produto: float = receber_valor_produto()
forma_de_pagamento: int = selecionar_formas_de_pagamento()
preco_produto, preco_final, exibir_forma_pagamento, exibir_desconto, valor_desconto = (
    calcular_desconto(preco_produto, forma_de_pagamento)
)
exibir_resultado(
    preco_produto, exibir_forma_pagamento, exibir_desconto, preco_final, valor_desconto
)
