# Faça um programa que calcule a soma de todos o números
# ímpares que são múltiplos de três e que se encontram no
# intervalo de 1 até 500

print('====== IMPRIMINDO NÚMEROS ÍMPARES ======')

somaImpares = 0

for contador in range(0, 501):
    if (contador % 2 != 0) and (contador % 3 == 0):
        somaImpares += contador
print(f'A soma dos números é: {somaImpares}')
