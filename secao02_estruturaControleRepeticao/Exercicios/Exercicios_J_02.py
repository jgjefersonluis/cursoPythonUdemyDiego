"""
Exercícios de fixação - Estrutura de repetição - While Curso de Python Exercício 2
---
O programa irá sortear um número entre 0 e 10.
O usuário precisará adivinhar qual foi o número que o computador sorteou.
Quando ele acertar, exiba quantas tentativas foram realizadas.
"""
import random

# Valor sorteado pelo computador
sorteado = random.randint(0, 10)

adivinhado = 99
tentativas = 0

while adivinhado != sorteado:
    tentativas += 1
    adivinhado = int(input('{}Qual o valor sorteado, entre 0 e 10)?' .format('\nIncorreto.\n\n' if adivinhado < 99 else '')))

print('\nVocê acertou o valor sorteado pelo computador {} em {} tentativas.'.format(adivinhado, tentativas))
