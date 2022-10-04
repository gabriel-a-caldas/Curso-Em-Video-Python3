# Crie um programa que mostre na tela todos os números 
# pares que estão no intervalo entre 1 e 50.

print('===== MOSTRANDO TODOS OS NÚMEROS PARES =====')

for contador in range(0, 51):
    if contador % 2 == 0:
        print(f'O número {contador} é par!')
print('FIM')
