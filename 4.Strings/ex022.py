# Faça um programa que leia um número de 0 a 9999 e mostre na tela
# cada um dos dígitos separados
# Exemplo: 
# Digite um número: 1834
# Unidade: 4
# Dezenda: 3
# Centena: 8
# Milhar: 1

numero = int(input('Insira um número: '))

# primeiroDigito = numero[0]
# segundoDigito = numero[1]
# terceiroDigito = numero[2]
# quartoDigito = numero[3]

quartoDigito = numero // 1 % 10
terceiroDigito = numero // 10 % 10
segundoDigito = numero // 100 % 10
primeiroDigito = numero // 1000 % 10

print(f'Unidade: {quartoDigito}')
print(f'Dezena: {terceiroDigito}')
print(f'Centena: {segundoDigito}')
print(f'Milhar: {primeiroDigito}')
