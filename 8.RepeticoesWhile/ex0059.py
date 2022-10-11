"""
Faça um programa que leia um número qualquer e mostre o seu fatorial.
"""

numero = int(input('Insira um número: '))

fatorial = 1

print(f'Calculando !{numero}: ', end=' ')
for i in range(numero,0,-1):
    print(i,end='')
    print(' x ' if i > 1 else ' = ', end='')
    fatorial = fatorial * i
print(fatorial, end='')

