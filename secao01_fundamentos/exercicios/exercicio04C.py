'''
Exercício 4
---
Leia um valor em metros, depois exiba esse valor em centímetros e milímetros.
'''

# Entrada do número
n = int(input('Quantos metros: '))

# Calcundo
cent = n * 100
mili = cent * 10

# Exibindo
print('Centímetros {} - Milímetros {}'.format(cent, mili))
