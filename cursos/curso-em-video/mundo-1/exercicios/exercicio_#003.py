# Crie um programa que leia dois números e mostre a soma entre eles.

print("\033[1;30;44mEscreva os números que deseja realizar a soma!\033[m")

primeiroNumero = int(input("Digite o primeiro número: "))
segundoNumero = int(input("Digite o segundo número: "))
resultado_soma = primeiroNumero + segundoNumero

print(f"\033[0;34mA soma entre os números escolhidos é:\033[m \033[1;36m{resultado_soma}\033[m")