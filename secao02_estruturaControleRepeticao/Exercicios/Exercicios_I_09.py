'''
Exercícios de Python Estrutura de Repetição
Exercício 9
---
Leia uma frase do usuário.
Exiba essa frase de trás para frente.
Exemplo: 'Curso de Python' --> 'nohtyP ed osruC
'''

frase = str (input('Digite uma frase: '))

for i in range(frase.__len__()-1,-1,-1):
    print(frase[i], end='')
