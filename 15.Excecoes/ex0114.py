"""
Crie um código em Python que testa se o site pudim está acessível pelo computador usado.
"""
import urllib
import urllib.request
from os import system

system('cls')

try:
    site = urllib.request.urlopen('http://www.pudim.com.br/')
except:
    print('O site pudim não está acessível no momento.')
else:
    print('Consegui acessar o site pudim com sucesso!')
