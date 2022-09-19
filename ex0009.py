# Crie um programa que leia quanto dinheiro
# uma pessoa tem na carteira e mostre quantos
# dólares ela pode comprar.
# Considere 1 US$ = R$5.16

dolar = 5.16

valorNaCarteira = int(input("Diga quanto dinheiro você tem na carteira: "))

valorEmDolar = valorNaCarteira/dolar
valorArrendodadoEmDolar = round(valorEmDolar,2)

print(f'Você consegue comprar: US${valorArrendodadoEmDolar}.')