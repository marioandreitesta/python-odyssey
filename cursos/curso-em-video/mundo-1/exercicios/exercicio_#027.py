# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente. 

DIV = 40

print('' * DIV)
nome_usuario = input('Digite seu nome completo: ').strip()
print('' * DIV)

nome_dividido = nome_usuario.split()

print(f'Seu primeiro nome é: {nome_dividido[0]}')
print(f'Seu último nome é: {nome_dividido[-1]}')