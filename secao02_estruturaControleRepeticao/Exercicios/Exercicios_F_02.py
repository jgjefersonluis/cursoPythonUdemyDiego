'''
Exercício 2
---
Pegunte ao usuário a velocidade do carro dele.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$130,16 para cada Km acima do limite de velocidade.
'''

velocidade = int(input('Qual a velocidade do seu carro em km/h?'))

if velocidade > 80:
    multa = (velocidade - 80) * 130.16
    print('Você foi multado em R$ {}. Reduza a velocidade!'.format(multa))
