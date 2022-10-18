"""
Exercícios de fixação - Estrutura de repetição - While
Curso de Python

Diego Mendes Rodrigues

Exercício 8
---
Iremos agora simular um caixa eletrônico, que possui notas de
R$50, R$20, R$10, R$5 e R$1.
O usuário irá digitar qual o valor que deseja sacar.
O script irá imprimir quantas células de cada valor serão entregues.
"""

valorSacado = int(input('Qual o valor R$ '))

faltaSacar = valorSacado
cedula = 50
totalDeCedulas = 0

while True:
    if faltaSacar >= cedula:
        faltaSacar -= cedula
        totalDeCedulas += 1
    else:
        if totalDeCedulas > 0:
            print('Total de {} cédulas de R$ {},00'.format(totalDeCedulas, cedula))

        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula = 1
        totalDeCedulas = 0

        if faltaSacar == 0:
            break