# Escreva um programa para aprovar o empréstimo bancário para a compra de
# uma casa. O programa vai perguntar o valor da casa, o salário do comprador
# e em quantos anos ele vai pagar.

# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do
# salário ou então o empréstimo será negado.

from time import sleep


print('-=-='*10)
print('ANALISADOR DE EMPRÉSTIMO BANCÁRIO')
print('-=-='*10)

valorCasa = float(input('Informe o valor da casa: '))
salario = float(input('Informe o valor do seu salário: '))
anosParaPagar = int(input('Informe em quantos anos deseja pagar: '))

print('ANALISANDO...')
sleep(3)

prestacao = valorCasa/(anosParaPagar*12)

if prestacao > (salario*0.3):
    print(f'EMPRÉSTIMO NEGADO! Infelizmente você não pode financiar esta casa.')
else:
    print(f'Você terá de pagar R${round(prestacao,2)} em prestações por mês!')
