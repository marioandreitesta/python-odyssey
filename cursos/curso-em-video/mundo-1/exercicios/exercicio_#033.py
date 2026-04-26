# Faça um programa que leia três números e mostre qual é o maior e qual é o menor. 

def pedir_numeros():

    while True:
        entrada = input("\n Digite três números separados por espaço: ")
        lista_numeros = entrada.split()

        if len(lista_numeros) != 3:
            print(f"Erro: Você digitou {len(lista_numeros)} valor(es). É preciso três!")
            continue

        try:
            numeros = list(map(float, lista_numeros))
            return numeros
        except ValueError:
            print("Oops! Certifique-se de digitar apenas números. Ex: 10 4.5 15")

def exibir_resultados():

    menor = min(numeros)
    maior = max(numeros)

    print("\n" + "=" * 38)
    print(f"Números digitados: {numeros}")
    print(f"Menor número: {menor}")
    print(f"Maior número: {maior}")
    print("=" * 38)

print("Detector de Menor e Maior!")
numeros = pedir_numeros()
exibir_resultados()