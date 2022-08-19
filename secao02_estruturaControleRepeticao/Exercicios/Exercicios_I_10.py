'''
Exercícios de Python -> Estrutura de Repetição

Exercício 10
---
Leia uma frase do usuário.
Exiba essa frase sem as vogais.
Exemplo: 'Curso de Python' --> 'Crs d Pythn'
'''

frase = str(input('Digite uma frase: '))

for c in frase:
    if c in 'aeiou':
        continue
    print(c, end=' ')