'''
Condições Aninhadas
'''

nome = str(input('Qual é o seu nome?'))

if nome == 'Diego':
    print('Que nome interessante.')
elif nome == 'Bruna' or nome == 'Regina':
    print('Nome de princesa!')
elif nome in 'Natalia Julia Amanda':
    print('Nome muito bonito!')
else:
    print('Seu nome é normal.')

print('Vá com cuidado {}.'.format(nome))
