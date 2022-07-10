# Atribuição Múltipla

x = 10
y = 20
a, b, c, d = 10, 20, 30, 40
print('{} {}'.format(x, y))
print('{} {} {} {}'.format(a, b, c, d))

# Operadores de Atribuição
# mais = menos = vezes = dividido = 2
#
mais = 2
mais += 2
print(mais)

menos = 0
menos -= 5
print(menos)

vezes = 2
vezes * 5
print(vezes)

dividido = 9
dividido /= 3
print(dividido)

# Atribuição Condicional

nota = 9
if nota >= 7:
    situacao = 'Aprovado'
else:
    situacao = 'Reprovado'

print('O aluno com nota {} está {}' .format(nota, situacao))


nota = 6
situacao = 'Aprovado' if nota >=7 else 'Reprovado'
print('O aluno com nota {} está {}' .format(nota, situacao))






