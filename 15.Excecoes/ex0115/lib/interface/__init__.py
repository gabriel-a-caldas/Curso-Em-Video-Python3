def leiaInt(mensagem):
    while True:
        try:
            numeroInteiro = int(input(mensagem))
        except (ValueError, TypeError):
            print('ERRO: Digite um número inteiro válido!')
            continue
        except (KeyboardInterrupt):
            print('O usuário decidiu não informar este número')
            return 0
        else:
            return numeroInteiro


def linha(tamanho=50):
    return '-' * tamanho


def cabecalho(mensagem):
    print(linha())
    print(f'{mensagem}'.center(len(linha())))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    for posicao, itens in enumerate(lista):
        print(f'{posicao+1} - {itens}')
    print(linha())
    opcao = leiaInt('Sua ooção: ')
    return opcao
