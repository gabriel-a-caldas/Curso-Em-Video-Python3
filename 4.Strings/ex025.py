# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A".
# Em que posição ela aparece a primeira vez.
# Em que posição ela aparece a última vez.

from re import A


frase = str(input('Insira a frase: ')).upper()

contaLetrasA = frase.count('A')
primeiraPosicao = frase.find('A')

print(f'Número de letras a: {contaLetrasA}')
print(f'Posição número: {primeiraPosicao}')