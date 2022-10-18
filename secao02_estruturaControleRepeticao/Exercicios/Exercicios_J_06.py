"""
Exercícios de fixação - Estrutura de repetição - While
Curso de Python

Exercício 6
---
Desenvolva um script que leia a idade e o sexo de várias pessoas.
Depois do cadastro de cada pessoa, o script deve perguntar para o usuário,
se ele deja ou não cadastrar uma nova pessoa.
No final, exiba na tela:
+ Quantas pessoas são maiores de idade
+ Quantos homens foram cadastrados
+ Quantas mulheres com mais de 21 anos foram cadastradas
"""

maiorDeIdade = 0
homens = 0
mulheresMais21 = 0

deseja = 'S'

while deseja == 'S':
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [H/M]: '))

    if idade >= 18:
        maiorDeIdade += 1

    if sexo.upper() == 'H':
        homens += 1
    elif sexo.upper() == 'M' and idade>21:
        mulheresMais21 += 1

    deseja = str(input('Deseja cadastrar outra pessoa [S/N]: ')).upper()

print('\nPessoas maoires de idade: {}'.format(maiorDeIdade))
print('Homens cadastrados: {}'.format(homens))
print('Mulheres com mais de 21 anos: {}'.format(mulheresMais21))
