'''
Exercício 3
---
Faça um programa que solicita o ano de nascimento de um garoto.
De acordo com a idade da pessoa, devemos mostrar:
Você irá se alistar no exército no futuro.
Esse é o ano para o seu alistamento.
Já passou o ano do seu alistamento.
'''
from datetime import datetime

ano = int(input('Qual é o seu ano de nascimento? '))

# Buscando o ano atual no sistema
dataAtual = datetime.now()
anoAtual = dataAtual.year

idade = anoAtual - ano

if idade == 18:
    print('Esse é o seu ano de alistamento. ')
elif idade < 18:
    print('Você irá se alistar dentro de {} anos. '.format(18 - idade))
else:
    print('Já passou o seu tempo de alistamento em {} anos.'.format(idade - 18))
