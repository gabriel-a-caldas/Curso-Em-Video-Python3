# Escreva um programa que leia um valçor em metros e
# o exiba convertido em centímetros e milímetros

valor = int(input("Insira um valor em metros : "))

valorCentimetros = valor*100
valorMilimetros = valor*1000

print(f'{valor} em centímetros é igual a: {valorCentimetros}cm. \n {valor} em milímetros é igual a {valorMilimetros}mm')