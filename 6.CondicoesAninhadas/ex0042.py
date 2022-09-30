# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule o seu IMC e mostre seu status, de acordo com a tabela abaixo:

# Abaixo de 18.5: Abaixo do Peso.
# Entre 18.5 e 25: Peso ideal.
# 25 até 30: Sobrepeso.
# 30 até 40: Obesidade.
# Acima de 40: Obesidade mórbida.

peso = float(input('Informe o seu peso: '))
altura = float(input('Informe a sua altura: '))

imc = round(peso/pow(altura,2),2)

if imc < 18.5:
    print(f'IMC: {imc}. Você está abaixo do peso!')
elif 18.5 <= imc <= 25:
    print(f'IMC: {imc}. Você está no peso ideal!')
elif 25 < imc < 30:
    print(f'IMC: {imc}. Você está sobrepeso!')
elif 30 < imc < 40:
    print(f'IMC: {imc}. Você está em estado de obesidade!')
else:
    print(f'IMC: {imc}. Você está em estado de obesidade mórbida!')