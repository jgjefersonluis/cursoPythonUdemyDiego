'''
Exercício 2
---
Leia um número e exiba na tela o seu dobro, o triplo e sua raiz quadrada.
Uma dica é que a raiz quadrada é a mesma coisa que realizarmos a potência de 0.5.
'''

# Entrada do número
n = int(input('Digite um número: '))

# Realizando os cálculos
dobro = n * 2
triplo = n * 3
raiz = n ** 0.5

# Exibindo na tela
print('Número {} - Dobro {} - Triplo {} - Raiz quadrada {:.1f}'. format(n, dobro, triplo, raiz))




