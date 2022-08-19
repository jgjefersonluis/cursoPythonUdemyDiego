'''
Exercícios de Python -> Estrutura de Repetição
Exercício 4
---
Solicite um número para o usuário final, depois exiba a tabuada desse
número utilizando o laço for.
'''

numero = int(input('Digite um número: '))

print('\nTabuada\n-------------------')

for i in range(1,11):
    print('{} x {} = {}'.format(i, numero, i * numero))
