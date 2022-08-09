'''
Uso do if e do else
Uso do and
'''

idade = int(input('Qual a sua idade?'))

if idade < 18:
    print('Apenas maiores de 18 anos podem entrar')
elif idade >= 18 and idade < 21:
    print('Você pode consumir refrigerantes')
else:
    print('Bem vindo!')
    bebida = str(input('Qual é a bebida que você deseja?'))
    print('A sua bebida é uma: {}'.format(bebida))
