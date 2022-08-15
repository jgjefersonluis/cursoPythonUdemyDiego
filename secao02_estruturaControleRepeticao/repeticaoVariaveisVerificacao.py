'''
Estruturas de Repetição - For, Variáveis e Controles com If
'''

# Utilizando variáveis
inicio = int(input('Início: '))
final = int(input('Final: '))
passo = int(input('Passo: '))

for num in range(inicio, final + 1, passo):
    print('Número {}'.format(num))

# Realizando a soma
print('')
soma = 0
for num in range(0, 3):
    n = int(input('Número: '))
    soma = soma + n
print('Soma = {}'.format(soma))

# Realizando a soma apenas de números entre 0 e 10
soma = 0
print('\nDigite apenas números entre 0 e 10.')

for num in range (0, 3):
    n = int(input('Número: '))
    if n >= 0 and n <= 10:
        soma = soma + n
    else:
        print('Serão somados apenas números entre 0 e 10, {} não será somado.'.format(n))

print('Soma = {}'.format(soma))
