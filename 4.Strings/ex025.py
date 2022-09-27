# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A".
# Em que posição ela aparece a primeira vez.
# Em que posição ela aparece a última vez.

frase = str(input('Insira a frase: ')).upper().strip()

contaLetrasA = frase.count('A')

primeiraPosicaoLetraA = frase.find('A')
ultimaPosicaoLetraA = frase.rfind('A')

print(f'A letra A aparece: {contaLetrasA} vezes.')
print(f'A primeira letra A aparece na posição: {primeiraPosicaoLetraA+1}')
print(f'A última letra A aparece na posição:  {ultimaPosicaoLetraA+1}')