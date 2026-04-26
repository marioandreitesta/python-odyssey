# Escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu armazenamento:
# Para salários superiores a R$1250,00, calcule um aumento de 10%;
# Para os inferiores ou iguais, o aumento é de 15%

def receber_salario():
    while True:
        try:
            salario_usuario = float(input("Digite o valor de seu salário [R$]: "))
            return salario_usuario
        except ValueError:
            print("Erro: é aceito apenas números, tente novamente!")

def calcular_aumento(salario):
    if salario > 1250:
        salario *= 1.10
        print(f"Seu salário recebeu um aumento de 10%: R${salario:.2f}")
    else:
        salario *= 1.15
        print(f"Seu salário recebeu um aumento de 15%: R${salario:.2f}")

salario_ajustado = receber_salario()
calcular_aumento(salario_ajustado)