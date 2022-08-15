'''
Estruturas de Repetição - For, Break e Continue
'''

# BREAK

# Utilizando o break para quebrar o laço do for quando num for igual a 2
print('Inicio')
for num in range(0, 6):
    print(num)
    if num == 2:
        break
print('Final')

# Exibindo textos, ou melhor, caracteres com o for
for c in 'Curso de Python':
    print(c)

# Exibindo textos e quebrando o laço quando o caracter for igual a 'o'
for c in 'Curso de Python' :
    print(c)
    if c == 'o':
        break

# CONTINUE

# Exibindo textos no laço, quando o caracter for igual a 'o', vote para o
# inicio do laço, ao invés de continuar com os comandos do laço
for c in 'Curso de Python':
    if c == 'o':
        continue
    print(c)

# Exibindo textos no laço, quando o caracter for igual a 'o', ou 'r', ou 'y',
# vote para o início do laço, ao invés de continuar com os comandos do laço

# BREAK

# Realizando a soma apenas de números entre 0 e 10.
# O valor máximo da soma será 20.
soma = 0
print('\Digite apenas números entre 0 e 10. \nA soma máxima será 20.')

for num in range(0, 4):
    n = int(input('Número: '))
    if n >= 0 and n <=10:
        soma = soma + n
    else:
        print('Serão somados apenas números entre 0 e 10, {} não será somado.'.format(n))

    if soma >= 20:
        soma = 20
        print('Valor máximo da soma atingido.')
        break

print('Soma = {}'.format(soma))
