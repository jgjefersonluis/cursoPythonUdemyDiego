"""
Exercícios de fixação - Estrutura de repetição - While
Curso de Python

Exercício 5
---
Exiba a tabuada de vários números, um de cada vez, para cada valor
digitado pelo usuário final. O script será interrompido quando
o valor digitado pelo usuário for negativo.
"""

tabuada = int(input('Qual o número para realizar a tabuada? '))

while tabuada >= 0:
    print('\nTabuada do {} -----------------'.format(tabuada))
    i = 1
    while i <=10:
        print('{} * {} = {}'.format(i, tabuada, i * tabuada))
        i += 1
    print('-------------------------------')

    tabuada = int(input('\nQual o número para realizar a tabuada? '))
