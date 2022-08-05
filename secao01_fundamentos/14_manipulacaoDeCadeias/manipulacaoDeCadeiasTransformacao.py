'''
Manipular as Cadeias de Caracteres - TRANSFORMAÇÃO
'''

'''
Cadeia de caracteres armazenada na memória com seus índices
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|C|u|r|s|o| |d|e| |P|y|t|h|o|n|
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
 0 1 2 3 4 5 6 7 8 9 10  ... 14
'''
# Cadeia de caracteres
frase = 'Curso de Python'

# Substituindo Python por PHP
print(frase.replace('Python', 'PHP'))

# Colocando todos os caracteres em maiúsculo
print(frase.upper())

# Colocando todos os caracteres em minúsculo
print(frase.lower())

# Colocando apenas a primeira letra da frase em maiúsculo
print(frase.capitalize())

# Colocando a primeira letra de cada palavra da frase em maiúsculo
print(frase.title())

# Nova cadeia de caracteres, com espaços inúteis no início e no final
frase = '   Aprendendo Python  '

# Exibindo na tela
print(frase)

# Removendo os caracteres inúteis do início e do final
print(frase.strip())

# Removendo os caracteres inúteis do início
print(frase.lstrip())

# Removendo os caracteres inúteis do final
print(frase.rsplit())
