# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa. 
DIV = 55

print("-"*DIV)
print("CALCULADORA DE HIPOTENUSA".center(DIV))
print("-"*DIV)

cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))
soma_catetos  = (cateto_oposto ** 2) + (cateto_adjacente ** 2)
hipotenusa = soma_catetos ** 0.5

print("-"*DIV)
print("Processando...".center(DIV))
print("-"*DIV)

print(f"O comprimento da hipotenusa é: {hipotenusa:.2f}")