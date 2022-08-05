'''
Exercício 2
---
O usuário irá digitar um número entre 0 e 999, então exiba cada um dos dígitos separados.
Exemplo: Número: 547
Unidade: 7
Dezena: 4
Centena: 5
'''

# ----
# Utilizando Inteiros
# ----
# Recebendo o número e convertendo em uma string
numero = int(input('Digite um número entre 0 e 999: '))
uni = numero // 1 % 10
dez = numero // 10 % 10
cen = numero // 100 % 10

# Exibindo
print('Unidade: {}'.format(uni))
print('Dezena: {}'.format(dez))
print('Centena: {}'.format(cen))

# ----
# Utilizando Strings
# ----
# Recebendo o número e convertendo em uma string
numero = str(input('Digite um número entre 0 e 999: '))

# Exibindo
print('Unidade: {}'.format(numero[2]))
print('Dezena: {}'.format(numero[1]))
print('Centena: {}'.format(numero[0]))
