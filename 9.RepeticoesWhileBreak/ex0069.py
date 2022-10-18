"""
Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar ao usuário se vai continuar.
No final, mostre:

a) Qual é o total gasto na compra.
b) Quantos produtos custam mais de R$1000,00.
c) Qual é o nome do produto mais barato.

"""

somaTotalProdutos = contadorMil = contador = menorValor = 0
produtoMaisBarato = ' '

print('='*22)
print('SUPERMERCADO MERCADÃO')
print('='*22)
while True:
    produto = str(input('Produto: ')).strip().upper()
    precoProduto = float(input('Preço: R$'))
    somaTotalProdutos += precoProduto
    contador += 1
    if precoProduto > 1000:
        contadorMil += 1
    if contador == 1 or precoProduto < menorValor:
        menorValor = precoProduto
        produtoMaisBarato = produto
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('DESEJA CONTINUAR? [S/N]: ')).strip().upper()[0]
    if escolha == 'N':
        break
print(f'O total da compra foi: R${round(somaTotalProdutos,2)}.')
print(f'Temos {contadorMil} produtos custando mais de R$1000,00.')
print(f'O produto mais foi: {produtoMaisBarato} barato custa R${menorValor}')