"""
Exercícios de fixação - Estrutura de repetição - While
Curso de Python
Exercício 1
---
Crie um script que leia o sexo de uma pessoa, aceitando apenas M ou F.
Caso o usuário digite um valor errado, solicite novamente até que seja digitado
o valor correto.
"""

sexo = str(input('Digite seu sexo [M/F]: ')).upper()

while sexo not in 'MF':
    print('\n\033[31mValor incorreto.\033[m Você deve digitar \033[1mM\033[m ou \033[1mF\033[m.\n')
    sexo = str(input('Digite seu sexo [M/F]: ')).upper()

print('\nO sexo escolhido foi o \033[4m{}\033[m.'.format('Feminino' if sexo == 'F' else 'Masculino'))
