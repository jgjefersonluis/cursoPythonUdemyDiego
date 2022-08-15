'''
Exercício 2
---
Pegunte ao usuário a velocidade do carro dele.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$5,00 para cada Km acima do limite de velocidade.
'''

velocidade = int(input('Qual é a velocidade do seu carro em km/h? '))

if velocidade > 80:
    multa = (velocidade - 80) * 5
    print('Você foi \033[4mmultado\033[m em \033[1mR$ {}\033[m. \033[1;31mReduza\033[m a velocidade!'.format(multa))





















