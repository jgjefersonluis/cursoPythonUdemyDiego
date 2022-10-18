"""
Exercícios de fixação - Estrutura de repetição - While Curso de Python  Exercício 3
---
Leia 2 valores inteiros do usuário.
Depois exiba um menu na tela:
1. Somar
2. Multiplicar
3. Maior valor
4. Entrar novos números
5. Sair
O usuário irá selecinar qual a opção desejada e mostrar o resultado,
depois exibirá o menu novamente.
"""

opcao = 0
num1 = int(input('Número 1: '))
num2 = int(input('Número 2: '))

while opcao != 5:
    print('-' * 20 + '\n      M E N U\n' + '-' * 20)
    print("1. Somar")
    print("2. Multiplicar")
    print("3. Maior valor")
    print("4. Entrar novos números")
    print("5. Sair")

    opcao = int(input('\nOpção desejada: '))

    if opcao == 1:
        print('\n{} + {} = {}\n'.format(num1, num2, num1 + num2))
    elif opcao == 2:
        print('\n{} x {} = {}\n'.format(num1, num2, num1 * num2))
    elif opcao == 3:
        print('\nMaior valor = {}\n'.format(num1 if num1 > num2 else num2))
    elif opcao == 4:
        num1 = int(input('\nNúmero 1: '))
        num2 = int(input('Número 2: '))
        print(' ')
