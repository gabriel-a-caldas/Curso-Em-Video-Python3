# Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso
# lidos.

maior = 0
menor = 0

for i in range(0, 5):
    peso = float(input('Informe o peso: '))
    menor = peso
    if peso > maior:
        maior = peso
    
print(f'O maior é {maior}.')
print(f'O menor é {menor}.')