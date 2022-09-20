# Faça um algortimo que leia o preço
# de um produto e mostre seu novo preço,
# com 5% de desconto.

price = int(input("Informe o preço do produto: "))

discount = price * (5/100)

newPrice = price - discount

print(f'O produto com 5% de desconto fica: {newPrice}')