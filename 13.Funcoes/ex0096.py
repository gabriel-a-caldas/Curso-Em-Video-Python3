"""
Faça um programa que tenha uma função chamada escreva(), que receba um texto
qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
Ex:
escreva('Olá, Mundo!')

Saída:
---------------
  Olá, Mundo!
---------------

"""
def escreva(mensagem):
    comprimentoMensagem = len(mensagem) + 4
    print('-'*comprimentoMensagem)
    print(f'  {mensagem}  ')
    print('-'*comprimentoMensagem)


mensagem = str(input('Digite uma mensagem: ')).strip()

escreva(mensagem)
