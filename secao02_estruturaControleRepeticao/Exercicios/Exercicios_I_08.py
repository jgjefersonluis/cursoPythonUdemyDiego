'''
Exercícios de Python -> Estrutura de Repetição

Exercício 8
---
Leia o peso de 5 pessoas.
Depois, mostre o maior e o menor pesos digitados.
'''

maiorPeso = 0
menorPeso = 99999

for i in range(0, 5):
    peso = int(input('Digite seu peso: '))

    if peso > maiorPeso:
        maiorPeso = peso

    if peso < menorPeso:
        menorPeso = peso

print('\nMaior peso: {}kg'.format(maiorPeso))
print('Menor peso: {}kg'.format(menorPeso))
