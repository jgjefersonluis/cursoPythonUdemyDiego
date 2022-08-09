'''
Uso do if e do else
'''

idade = int(input('Qual a sua idade?'))

if idade < 18:
    print('Apenas maiores de 18 anos podem entrar')
# if idade >=18:
else:
    print('Olá! Aproveite o nosso bar!')
    bebida = str(input('Qual é a bebida que você deseja?'))
    print('A sua bebida é: {}'.format(bebida))
    