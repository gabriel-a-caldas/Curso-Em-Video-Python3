# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

print('========= VERIFICADOR DE NÚMEROS PRIMOS ========')

numero = int(input('Insira um número: '))

contador = 0

for i in range(1,numero+1):
    if numero % i == 0:
        contador += 1
if contador == 2 or contador ==1:
    print(f'{numero} é primo!')
elif contador > 2:
    print(f'{numero} não é primo!')