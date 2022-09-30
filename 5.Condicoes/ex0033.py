# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
# Para salarios superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Insira o valor do seu salário: '))

aumentoDezPorcento = salario * 0.10
aumentoQuinzePorcento = salario * 0.15

if salario > 1250:
    print(f'Você recebeu um aumento de {aumentoDezPorcento}! Seu salário será: {salario+aumentoDezPorcento}')
elif salario <= 1250:
    print(f'Você recebeu um aumento de {aumentoQuinzePorcento}! Seu salário será: {salario+aumentoQuinzePorcento}')
