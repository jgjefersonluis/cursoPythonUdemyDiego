'''
Exercício 1
---
Crie um script para aprovar um empréstimo bancário.
Devemos perguntar para o usuário: o valor do imóvel; o salário; em quantos anos
será realizado o pagamento.
Então devemos calcular a prestação mensal, sabendo que ela não pode ser maior
do que 30% do salário, que neste caso, o empréstimo não será aprovado.
'''

valor = float(input('Valor do imóvel R$ '))
salario = float(input('Valor do seu salário R$ '))
anos = int(input('Em quantos anos será realizado o pagamento? '))

meses = anos * 12
prestacaoMensal = valor/meses
valorPermitidoPrestacao = salario * 0.3

if prestacaoMensal <= valorPermitidoPrestacao:
    print('Parabéns! Empréstimo aprovado com a prestação de R$ {:.2f}.'.format((prestacaoMensal)))
else:
    print('Desculpe mas não podemos aprovar o seu empréstimo.')
    print('O valor de R$ {:.2f} é maior do que podemos aprovar de acordo com o seusalário, que é R$ {:.2f}'.format(prestacaoMensal, valorPermitidoPrestacao))








