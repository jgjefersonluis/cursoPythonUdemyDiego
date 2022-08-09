'''
Exercício 4
---
Desenvolva um calculadora de preços de passagens. Será cobrado R$0,60 por Km
para viagens de até 100Km e R$0,50 para viagens mais longas.
'''

distancia = int(input('Qual a distancia da viagem em km?'))

passagem = 0.0
if distancia <= 100:
    passagem = distancia * 0.6
else:
    passagem = distancia * 0.5

print('Valor da passagem: R$ {:.2f}'.format(passagem))

