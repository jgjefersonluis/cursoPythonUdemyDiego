'''
Exercício 1
---
Crie um script onde o usuário digita um número inteiro, então você exibe na tela o
seu sucessor e o seu antecessor.
'''

# Entrada do número
n = int(input('Digite um número: '))

# Exibição do sucessor e do antecessor
print('Numero {} - Sucessor {} - Antecessor {}'.format(n, n+1, n-1))