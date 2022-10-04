# Refaça o desafio 009, mostrando a tabuada de um número que
# o usuário escolher, só que agora utilizando um laço for.

from audioop import mul


numero = int(input('Insira qual número você deseja a tabuada: '))
numeroMultiplos = int(input('Informe quantos múltiplos você deseja: '))

print(f'======== TABUADA DE {numero} ========')

for i in range(0,numeroMultiplos+1):
    print(f' {numero} x {i} = {i*numero}')
