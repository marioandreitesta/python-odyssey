# Escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu armazenamento:
# Para salários superiores a R$1250,00, calcule um aumento de 10%;
# Para os inferiores ou iguais, o aumento é de 15%

from cores import LIMPAR, CINZA_BOLD, AZUL_BOLD, VERDE_BOLD, VERMELHO_BOLD

def receber_salario():
    
    while True:
        try:
            salario_usuario = float(input(f"{AZUL_BOLD}Digite o valor de seu salário [R$]: {LIMPAR}"))
            return salario_usuario
        except ValueError:
            print(f"{LIMPAR}{VERMELHO_BOLD}Erro: {CINZA_BOLD}é aceito apenas números, tente novamente!{LIMPAR}")

def calcular_aumento(salario):

    if salario > 1250:
        salario *= 1.10
        print(f"{AZUL_BOLD}Seu salário recebeu um aumento de {CINZA_BOLD}10%: {VERDE_BOLD}R${CINZA_BOLD}{salario:.2f}{LIMPAR}")
        
    else:
        salario *= 1.15
        print(f"{AZUL_BOLD}Seu salário recebeu um aumento de {CINZA_BOLD}15%: {VERDE_BOLD}R${CINZA_BOLD}{salario:.2f}{LIMPAR}")

salario_ajustado = receber_salario()
calcular_aumento(salario_ajustado)