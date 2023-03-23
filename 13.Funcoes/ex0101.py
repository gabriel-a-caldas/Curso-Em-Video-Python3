"""
Crie uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal se uma pessoal tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
"""
def voto(anoNascimento):
    """
    Verifica baseado na idade, se o voto é NEGADO
    OPCIONAL ou OUBRIGATÓRIO.
    :param idade: inteiro -> Idade do usuário.
    """
    from datetime import date

    anoAtual = date.today().year
    idade = anoAtual - anoNascimento

    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'

# Programa principal
print('-'*40)
idade = int(input("Em que ano você nasceu? "))

print(voto(idade))