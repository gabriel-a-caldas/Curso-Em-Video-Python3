"""
Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar ao usuário se vai continuar.
No final, mostre:

a) Qual é o total gasto na compra.
b) Quantos produtos custam mais de R$1000,00.
c) Qual é o nome do produto mais barato.

"""

somaTotalProdutos = contadorProdutoMilReais = produtoMaisBarato = 0
nomeProdutoMaisBarato = ''

while True:
    print('='*22)
    print('SUPERMERCADO MERCADÃO')
    print('='*22)
    nomeProduto = str(input('Nome do produto: ')).strip()
    precoProduto = float(input('Preço: R$'))
    produtoMaisBarato = precoProduto
    escolha = str(input('DESEJA CONTINUAR? [S/N]: ')).strip().upper()
    while escolha != 'S' and escolha != 'N':
        escolha = str(input('DESEJA CONTINUAR? [S/N]: ')).strip().upper()
    somaTotalProdutos += precoProduto
    if escolha == 'N':
        break
    if precoProduto > 1000:
        contadorProdutoMilReais += 1
    if precoProduto < produtoMaisBarato:
        produtoMaisBarato = precoProduto
        nomeProdutoMaisBarato = nomeProduto
print(f'O total da compra foi: R${round(somaTotalProdutos,2)}.')
print(f'Temos {contadorProdutoMilReais} produtos custando mais de R$1000,00.')
print(f'O produto mais barato: {nomeProdutoMaisBarato} que custa R${produtoMaisBarato}')