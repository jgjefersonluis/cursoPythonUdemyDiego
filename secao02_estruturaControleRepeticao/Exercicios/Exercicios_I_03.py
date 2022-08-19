'''
Exercícios de Python -> Estrutura de Repetição

Exercício 3
---
Calcule a soma de todos os números ímpares que são múltiplos de 3
no intervalo de 1 até 500.
'''

print('Soma dos números ímpares de 1 até 500 múltiplos de 3:')

soma = 0

for i in range(1, 501, 2):      # Números ímpares
    if i % 3 == 0:              # Utilizando o resto da divisão inteira para verificar
        print(i)                # se o número é multiplo de 3
        soma += 1

print('Soma = {}'.format(soma))
