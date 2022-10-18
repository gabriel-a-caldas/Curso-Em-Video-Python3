"""
Crie um programa que simule o funcionamento de um caixa eletrônico. No
início, pergunte ao usuário qual será o valor a ser sacado (numero inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.

OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""

quantidadeNotasUm = quantidadeNotasDez = quantidadeNotasVinte = quantidadeNotasCinquenta = 0
unidade = centena = dezena = milhar = total = 0

while True:
    quantidade = int(input('VALOR DE SAQUE: '))

    unidade = quantidade // 1 % 10
    dezena = (quantidade // 10 % 10)
    centena = (quantidade // 100 % 10)
    milhar = (quantidade // 1000 % 100)

    if dezena%2 == 0:
        quantidadeNotasVinte = (dezena * 10)/ 20
        print(f'Foram usadas: {quantidadeNotasVinte} notas de R$20.')
        break
    else:
        quantidadeNotasVinte = (dezena * 10) // 20
        quantidadeNotasDez = ((dezena * 10) // 10) - quantidadeNotasVinte*2
        print(f'Foram usadas: {quantidadeNotasVinte} notas de R$20 e {quantidadeNotasDez} notas de R$10.')
    break