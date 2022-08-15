'''
Estruturas de Repetição - While
'''

'''
Enquanto n1 e n2 forem diferentes de zero
    Entre com o número 1
    Entre com o número 2
    Soma = número 1 + número 2
    Exibir Soma
'''

num1 = 1
num2 = 0
soma = num1 + num2

while soma > 0:
    num1 = int(input('Número 1: '))
    num2 = int(input('Número 2: '))
    soma = num1 + num2
    print('{} + {} = {}\n'.format(num1, num2, soma))

numero = 7
while numero >= 3:
    print(numero)
    numero = numero - 1
