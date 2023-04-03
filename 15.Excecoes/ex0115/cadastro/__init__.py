def cabecalho(mensagem):
    print('-'*50)
    print(f'{mensagem}'.center(50))
    print('-'*50)

def cadastraPessoas(nome, idade):
    with open('pessoasCadastradas.txt','a',encoding='utf-8') as arquivo:
        arquivo.write(f'{nome}')
        arquivo.write(f'{idade} anos'.rjust(50-len(nome)))
        arquivo.write('\n')


def consultaPessoas():
    with open('pessoasCadastradas.txt','r',encoding='utf-8') as arquivo:
        mensagem = arquivo.readlines()
    cabecalho('PESSOAS CADASTRADAS')
    for pessoas in mensagem:
        print(pessoas)
