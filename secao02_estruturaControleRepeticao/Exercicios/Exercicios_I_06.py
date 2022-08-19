'''
Exercícios de Python -> Estrutura de Repetição
Exercício 6
---
O usuário irá digitar um número, depois o script irá dizer se
esse é um número primo.
'''

numero = int(input('Digite um número: '))

# O número primo só pode ser dividido por 1 e por ele mesmo
# Exemplo: 5 é primo, pois ele é divisível apenas por 1 e por 5 (2 divisões)
# 6 NÃO é primo, pois ele é divisível por 1, 2, 3 e 6 (4 divisões)

totalDeDivisoes = 0

print('\nOs divisores irão aprecer em vermelho.\n')

for i in range(1, numero+1):
    if numero % i == 0:
        totalDeDivisoes += 1
        print('\033[31m', end=' ')
    else:
        print('\033[m', end=' ')
    print('{}'.format(i), end=' ')

print('\n\n\033[mO número {} possui {} divisores, então '.format(numero, totalDeDivisoes), end='')

if totalDeDivisoes == 2:    # Números primos só possuem 2 divisores, o 1 e ele mesmo
    print('ele é PRIMO.')
else:
    print('ele NÃO é PRIMO.')
