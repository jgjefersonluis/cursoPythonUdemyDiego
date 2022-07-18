'''
Exercício 6
---
Solicite que a pessoa digite quanto ela tem de dinheiro na carteira.
Depois, exiba quantos dólares ela possui, usando a conversão US$ 1,00 = R$ 3,3
'''

# Entrada do número de reais
n = float(input('Quantos reais você possui R$: '))

# Calculando os dólares
dolares = n/5.3

# Exibindo
print('Você possui US$ {:.2f} dólares.'.format(dolares))
