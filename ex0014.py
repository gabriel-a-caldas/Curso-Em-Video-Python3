# Escreva um programa que pergunte a quantidade de km percorridos
# por um carro alugado e a quantidade de dias pelos quais ele fpo
# alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00
# por dia e R$0,15 por km rodado.

quantidadeQuilometros = int(input('Informe a quantidade de quilômetros percorridos: '))
quantidadeDias = int(input('Informe a quantidade de dias que você esteve com o carro: '))

valorAluguel = (quantidadeQuilometros * 0.15) + (quantidadeDias * 60)

print(f'Por ter passado {quantidadeDias} dias e andado {quantidadeQuilometros} km com o carro, o valor do alguel foi de: R${valorAluguel}.')