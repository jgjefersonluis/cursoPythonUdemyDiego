'''
Exercício 8
---
No script o usuário digita o valor de um produto, depois você mostra um novo
valor com 10% de desconto.
'''

# Entrada do valor do produto
valor = float(input('Valor do produto R$: '))

# Calculando o desconto de 10%
valorComDesconto = valor * 0.90

# Exibindo
print('Valor com desconto de 10% R$ {:.2f}'.format(valorComDesconto))

