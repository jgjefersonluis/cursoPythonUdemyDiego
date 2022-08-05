'''
Exercícios de Python para a assimilação do conteúdo já apresentado
Curso de Python

Diego M. Rodrigues

Exercício 1
---
Crie um script onde o usuário digita 2 números e você exibe a soma deles.
'''

# Recebendo os valores do usuário e convertendo para inteiro
n1 = int(input('Número 1: '))
n2 = int(input('Número 2: '))

# Realizando a soma
soma = n1 + n2

# Exibindo o resultado
print('A soma de {} e {} vale {}'.format(n1, n2, soma))