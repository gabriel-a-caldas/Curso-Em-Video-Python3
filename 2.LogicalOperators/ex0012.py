# Faça um algoritmo que leia o salário de um funcionário
# e mostre seu novo salário, com
# 15% de aumento

salario = float(input('Informe o seu salário: '))

aumento = salario * (15/100)

novoSalario = salario + aumento

round(novoSalario,2)

print(f'Seu novo salário com 15% de aumento é R${novoSalario}')