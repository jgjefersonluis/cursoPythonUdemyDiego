'''
Exercício 3
---
Faça um programa que o usuário entre com um número inteiro e você mostra na
tela se ele é par ou ímpar.
'''

numero = int(input('Digite um número inteiro: '))

# Usando o resto da divisão para saber se o número é par ou impar
if numero % 2 == 0:
    print('Número \033[1;33mpar\033[m')
else:
    print('Número \033[1;34mimpar\033[m')