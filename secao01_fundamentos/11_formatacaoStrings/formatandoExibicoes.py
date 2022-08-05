cor = input('Escolha uma cor: ')

# Alinhamentos
print('Cor escolhida {:>10}.'.format(cor))
print('Cor escolhida {:<10}.'.format(cor))
print('Cor escolhida {:=^10}.'.format(cor))

# Utilizando dois números
n1 = 7
n2 = 3

print('Soma {}'.format(n1+n2))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

# Exibindo a soma, multiplicação e a divisão
print('Soma {} Multiplicação {} Divisão {}'.format(s,m,d))

# Formatando o float com 2 casas decimais
print('Soma {} Multiplicação {} Divisão {:.2f}'.format(s,m,d))

# Removendo a quebra de linha no print()
print('Soma {} Multiplição {} Divisão {:.2f}'.format(s,m,d), end=' ')
print('Divisão Inteira {} Potência {}'. format(di, e))
