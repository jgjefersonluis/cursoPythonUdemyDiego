'''
Exercício 6
---
Desenvolva um programa que calcule o valor a ser pago de um produto em uma
livraria, considerando o preço normal e a condição de pagamento:
À vista com dinheiro - 10% de desconto.
À vista com cartão - 5% de desconto.
Em 2 vezes no cartão - Preço normal.
3 ou mais vezes no cartão - 20% de juros.
'''


valorNormal = float(input('Qual o valor normal do livro R$ '))

print('Formas de pagamento:')
print('1 - À vista com dinheiro')
print('2 - À vista com cartão')
print('3 - Em 2 vezes no cartão')
print('4 - 3 ou mais vezes no cartão')

forma = int(input('Qual a sua forma de pagamento? '))

if forma < 1 or forma > 4:
    print('Forma de pagamento inválida')
elif forma == 1:
    print('Valor que deve ser pago R$ {:.2f}'.format(valorNormal*0.90))
elif forma == 2:
    print('Valor que deve ser pago R$ {:.2f}'.format(valorNormal*0.95))
elif forma == 3:
    print('Valor que deve ser pago R$ {:.2f}'.format(valorNormal))
else:
    print('Valor que deve ser pago R$ {:.2f}'.format(valorNormal*1.2))












