# Faça um programa que leia um número de 0 a 9999 e mostre na tela
# cada um dos dígitos separados
# Exemplo: 
# Digite um número: 1834
# Unidade: 4
# Dezenda: 3
# Centena: 8
# Milhar: 1

numero = str(input('Insira um número: '))

primeiroDigito = numero[0]
segundoDigito = numero[1]
terceiroDigito = numero[2]
quartoDigito = numero[3]

print(f'Unidade: {quartoDigito}')
print(f'Dezena: {terceiroDigito}')
print(f'Centena: {segundoDigito}')
print(f'Milhar: {primeiroDigito}')
