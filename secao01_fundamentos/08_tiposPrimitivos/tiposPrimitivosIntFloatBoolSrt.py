# Tipo INT
n1 = int(input('Número 1: '))
n2 = int(input('Número 2: '))
type(n1)

soma = n1 + n2
type(soma)

print('A soma de {} e {} vale {}'.format(n1, n2, soma))

# Tipo FLOAT
n3 = float(input('Seu peso: '))
print(type(n3))
print((n3))

# Tipo BOOL
n4 = bool(input('Seu nome: '))
print(type(n4))
print(n4)

# Tipo STR
n = input('Usuário: ')
print(type(n))
print(n)

print(n.isalnum())
print(n.isalpha())
print(n.isnumeric())
print(n.islower())
print(n.isascii())

