# Desenvolva um programa que pergunte a distãncia de uma viagem em Km
# Calcule o preço da passagem, cobrando R$0,50 por km para viagens
# até 200 km e R$ 0,45 para viagens mais longas

distancia = float(input('Informe a distância da viagem: '))

if distancia < 200:
    valorFinal = distancia * 0.50
    print(f'Sua passagem ficou em: R${valorFinal}')
else:
    valorFinal = distancia * 0.45
    print(f'Sua passagem ficou em: R${valorFinal}')