"""
Exercícios de fixação - Estrutura de repetição - While
Curso de Python

Exercício 4
---
Leia vários números inteiros do usuário, sendo que o script irá parar
quando for digitado o valor 999.
No final, mostre quantos valores foram digitados e a soma deles,
desconsiderando a condição de parada 999.
"""

soma = 0
quantidade = 0
num = 0

print('Realize a soma dos números desejados, entre 0 e 998.')
print('Para finalizar a soma digite 999.\n')

while True:
    num = int(input('Digite um número: '))
    if num != 999:
        soma += num
        quantidade += 1
    else:
        break

print('Foram digitados {} valores, sendo o valor da soma deles {}.'.format(quantidade, soma))