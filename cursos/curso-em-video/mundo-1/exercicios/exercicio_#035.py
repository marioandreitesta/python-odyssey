# Desenvolva um programa que leia três retas e diga ao usuário se elas podem ou não formar um triângulo. 

def receber_comprimento():

    while True:
        entrada = input("\n Digite três comprimentos separados por espaço: ")
        lista = entrada.split()

        if len(lista) != 3:
            print(f"Você digitou {len(lista)}, é preciso de exatamente três.")
            continue

        try:
            comprimentos = list(map(float, lista))
            return comprimentos
        
        except ValueError:
            print("Error: Use apenas números. Ex: 20, 12, 3.7")

def calcular_triangulo(comprimentos):

    a = comprimentos[0]
    b = comprimentos[1]
    c = comprimentos[2]

    if a + b > c and a + c > b and b + c > a: # Condição de Existência de um Triângulo
        print("Os comprimentos informados podem formar um triângulo!")
    else:
        print(f"Os comprimentos informados {comprimentos} não podem formar um triângulo.")

comprimentos = receber_comprimento()
calcular_triangulo(comprimentos)
