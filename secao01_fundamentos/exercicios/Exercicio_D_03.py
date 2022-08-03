'''
Exercício 3
---
Um professor quer sortear um dos seus 3 alunos para apagar o quadro.
Leia o nome desses 3 alunos e depois exiba na tela o escolhido.
Módulo: random
'''

# Importando o módulo random
import random

nome1 = str(input('Nome do aluno 1: '))
nome2 = str(input('Nome do aluno 2: '))
nome3 = str(input('Nome do aluno 3: '))

# criando uma lista com o nome dos alunos
alunos = [nome1, nome2, nome3]

# Sorteando o escolhido
escolhido = random.choice(alunos)

# Exibindo
print('Escolhido: {}'. format(escolhido))
