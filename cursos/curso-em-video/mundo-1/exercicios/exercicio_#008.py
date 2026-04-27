# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros. 

print("Conversor de Metros!")

metros = float(input("Digite a metragem que deseja converter: "))

CENTIMETROS = metros * 100
MILIMETROS = metros * 1000

print(f"{metros:.0f} metro(s) em:")
print(f"Centímetros: {CENTIMETROS:.0f}cm")
print(f"Milímetros: {CENTIMETROS:.0f}mm")