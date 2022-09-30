# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A".
# Em que posição ela aparece a primeira vez.
# Em que posição ela aparece a última vez.

<<<<<<< HEAD
from re import A


frase = str(input('Insira a frase: ')).upper()

contaLetrasA = frase.count('A')
primeiraPosicao = frase.find('A')

print(f'Número de letras a: {contaLetrasA}')
print(f'Posição número: {primeiraPosicao}')
=======
frase = str(input('Insira a frase: ')).upper().strip()

contaLetrasA = frase.count('A')

primeiraPosicaoLetraA = frase.find('A')
ultimaPosicaoLetraA = frase.rfind('A')

print(f'A letra A aparece: {contaLetrasA} vezes.')
print(f'A primeira letra A aparece na posição: {primeiraPosicaoLetraA+1}')
print(f'A última letra A aparece na posição:  {ultimaPosicaoLetraA+1}')
>>>>>>> bd18eac93bc54cb541127c7aa5e6f2b359103702
