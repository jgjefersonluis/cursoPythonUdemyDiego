'''
Exercício 2
---
Solicite 2 números inteiros para o usuário final.
Depois você deve comparar os números para exibir uma das seguintes mensagens:
O primeiro valor é maior que o segundo.
O segundo valor é maior que o primeiro.
Os dois valores são iguais.
'''

num1 = int(input('Número 1: '))
num2 = int(input('Número 2: '))

if num1 == num2:
    print('Os dois valores são iguais.')
else:
    if num1 > num2:
        print('O primeiro valor é maior que o segundo.')
    else:
        print('O segundo valor é maior que o primeiro.')