"""
Exercícios de fixação - Estrutura de repetição - While
Curso de Python

Diego Mendes Rodrigues

Exercício 7
---
Desenvolva um script que leia o nome e o valor de vários produtos de uma loja.
Depois de cada lançamento, o script deve perguntar para o usuário,
se ele deja ou entrar com outro produto.
No final, exiba na tela:
+ O total dos gastos na loja
+ Quantos produtos custam mais que R$ 100,00
+ Qual o nome do produto de menor valor
"""

totalGastos = 0
quantosMais100 = 0
nomeProdutoMenorValor = ''
valorProdutoMenorValor = 999999

deseja = 'S'

while deseja == 'S':
    nome = str(input('Nome do produto: '))
    valor = float(input('Valor R$: '))

    totalGastos += valor

    if valor > 100:
        quantosMais100 += 1

    if valor < valorProdutoMenorValor:
        valorProdutoMenorValor = valor
        nomeProdutoMenorValor = nome

    deseja = str(input('Deseja lançar outro produto [S/N]: ')).upper()

print('\nTotal dos gastos: R$ {:.2f}'.format(totalGastos))
print('Quantos produtos custam mais que R$ 100,00: {}'.format(quantosMais100))
print('Produto de menor valor: {} que é R$ {:.2f}'.format(nomeProdutoMenorValor, valorProdutoMenorValor))