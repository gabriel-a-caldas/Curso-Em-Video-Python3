"""
Crie um programa em que o usuário digite uma expressão que use parênteses.
Seu aplicativo deverá analisar se a exressão passada está com os parênteses
abertos e fechados na ordem correta.
"""
expressaoNumerica = list(str(input('Digite uma expressão: ')).replace(' ',''))

for elementoExpressao in expressaoNumerica:
    contaParentesesInicial = expressaoNumerica.count('(')
    contaParentesesFinal = expressaoNumerica.count(')')

if expressaoNumerica[0] == ')':
    print('Expressão incorreta!')
elif contaParentesesInicial != contaParentesesFinal:
    print('Expressão incorreta!')
else:
    print('Expressão correta!')
