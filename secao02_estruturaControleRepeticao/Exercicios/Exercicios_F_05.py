'''
Exercício 5
---
Faça um script em que o usuário digita um ano, então deve ser informado
se o ano é ou não bissexto.
'''

numero = int(input('Digite um ano: '))

# Usando o resto da divisão para saber se o ano é bissexto
if numero%4 == 0:
    print('Ano bissexto')
else:
    print('Esse ano não é bissexto')
