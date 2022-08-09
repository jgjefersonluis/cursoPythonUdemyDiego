'''
Exercício 3
---
Faça um programa que o usuário entre com um número inteiro e você mostra na
tela se ele é par ou ímpar.
'''

numero = int(input('Digite um número inteiro: '))

# Usando o resto da divisão para saber se o número é par ou ímpar
if numero % 2 == 0:
    print('Número par')
else:
    print('Número ímpar')
