# Faça um programa que leia algo pelo teclado
# e mostre na tela o seu tipo primitivo e todas
# as informações sobre ela.

variavel = input('Digite algo: ')

print('O tipo desta variável é', type(variavel))
print('Só tem espaços? ', variavel.isspace())
print('É um número? ', variavel.isnumeric())
print('É alfabético? ', variavel.isalpha())
print('Está em maiúsculo? ', variavel.isupper())
print('Está em minúsculo? ', variavel.islower())
print('Está capitalizada?', variavel.istitle())
