'''
Exercício 3
---
Faça um script que leia as duas notas de um aluno, depois mostra a sua média.
Lembre de utilizar o print com o format, além de prestar atenção na ordem de
precedência dos operadores.
'''

# Entrada das notas
nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))

# Calculando a média
media = (nota1 + nota2) / 2

# Exibindo a média
print('Media {:.2f}'.format(media))
