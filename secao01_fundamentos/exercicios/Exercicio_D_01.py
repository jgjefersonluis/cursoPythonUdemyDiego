'''
Exercício 1
---
Crie um script que leia um número real e mostre na tela sua parte inteira.
Exemplo: Número 5.165 - Inteira 5
'''

# importando o módulo math
import math

# Recebendo um número real
num = float(input('Digite um número real: '))

# Mostrando a parte inteira com math.trunc()
print('Número {} - Parte inteira {}'. format(num, math.trunc(num)))
