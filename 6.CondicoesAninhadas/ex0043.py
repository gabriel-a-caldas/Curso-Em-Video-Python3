# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# À vista dinheiro/cheque: 10% de desconto
# À vista no cartão: 5% de desconto
# Em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros.

valorASerPago = float(input('Informe o valor a ser pago: '))
condicaoPagamento = int(input('Informe as condições de pagamento: \n 1 - Dinheiro/cheque. \n 2 - À vista no cartão \n 3 - Em 2x no cartão. \n 4 - Em 3x ou mais no cartão. \n Escolha: '))

if condicaoPagamento == 1:
    desconto = valorASerPago * 0.1
    print(f'Você ganhou: R${desconto}. Pague: R${valorASerPago-desconto}.')
elif condicaoPagamento == 2:
    desconto = valorASerPago * 0.05
    print(f'Você ganhou: R${desconto}. Pague: R${valorASerPago-desconto}.')
elif condicaoPagamento == 3:
    print(f'Você deve pagar duas parcelas de R${valorASerPago/2}')
elif condicaoPagamento == 4:
    juros = 0.2 * valorASerPago
    print(f'Temos um pequno juros de R${juros}. Você deverá pagar R${valorASerPago+juros} em quantas parcelas desejar!')
