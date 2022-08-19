'''
Exercícios de Python -> Estrutura de Repetição

Exercício 7
---
Crie um script que leia o ano de nascimento de 5 pessoas.
Depois o script mostra quantas pessoas já atingiram a maioridade
e quantas não atingiram.
Dica: Maior de idade é quem já possui 18 anos ou mais.
'''
from datetime import datetime

totalMaiores = 0
totalMenores = 0

anoAtual = datetime.now().year

for i in range(0, 5):
    ano = int(input('Ano de nascimento: '))
    if anoAtual - ano >= 18:
        totalMaiores += 1
    else:
        totalMenores += 1

print('\nMaiores = {}'.format(totalMaiores))
print('Menores = {}'.format(totalMenores))
