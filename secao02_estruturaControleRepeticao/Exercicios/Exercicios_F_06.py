'''
Exercício 6
---
Escreva um programa para calcular aumentos de funcionários de uma lanchonete.
Para funcionários que recebam mais de R$1500,00 o aumento será de 10%, enquanto
que para os funcionários com salários mais baixos o aumento será de 20%.
'''

salario = float(input('Valor atual do salário: R$ '))

salarioComAumento = 0.0

if salario > 1500:
    salarioComAumento = salario * 1.1 # Aumento de 10%
else:
    salarioComAumento = salario * 1.2 # Aumento de 20%

print('Novo salário: R$ {:.2f}'.format(salarioComAumento))
