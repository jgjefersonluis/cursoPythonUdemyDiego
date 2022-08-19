'''
Exercícios de Python -> Estrutura de Repetição
---
Crie um script que leia 6 números inteiros do usuário.
Mostre a soma apenas dos números pares que foram digitados.
'''

soma = 0

for i in range(0,6):
    num = int(input('Número {}: '.format(i+1)))

    if num%2 == 0:      # Utilizando o resto da divisão para determinar
        soma += num     # os números pares

print('Soma dos números pares = {}'.format(soma))

# Outra solução: Encontrar o número ímpar e usar o 'continue' para saltar
# novamente para o início do laó

# for i in range(0,6):
#     num = int(input('Número {}: '.format(i+1)))
#
#     if num%2 == 1:      # Utilizando o resto da divisão para determinar
#         continue        # os números ímpares
#
#     soma += num

# print('Soma dos números pares = {}'.format(soma))
