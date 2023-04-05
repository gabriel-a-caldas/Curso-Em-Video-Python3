from lib.interface import *
from time import sleep

def cadastraPessoas():
    nomeUsuario = str(input('Nome: ')).strip()
    idade = leiaInt('Idade: ')
    tamanhoNome = 50-len(nomeUsuario)
    with open("15.Excecoes\ex0115\cadastro.txt",'a',encoding='UTF-8') as bancoDados:
        bancoDados.write(f'{nomeUsuario}')
        bancoDados.write(f'{idade}\n'.rjust(tamanhoNome))
    print(f'Novo registro: {nomeUsuario} adicionado com sucesso!')
    sleep(2)


def exibePessoasCadastradas():
    with open("15.Excecoes\ex0115\cadastro.txt",'r',encoding='UTF-8') as listaPessoasCadastradas:
        cabecalho('PESSOAS CADASTRADAS')
        for pessoas in listaPessoasCadastradas:
            print(pessoas.replace('\n',''))
        sleep(1)
