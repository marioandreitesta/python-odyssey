# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = input('Digite seu nome completo: ').strip()

nome_formatado = nome.upper()
nome_verificador = 'SILVA'

if nome_verificador in nome_formatado:
    print('Seu nome tem a palavra "Silva"')
else:
    print('Seu nome não tem "Silva"')