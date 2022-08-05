'''
Manipular as Cadeias de Caracteres - FATIAMENTO
'''

'''
Cadeia de caracteres armazenada na memória com seus índices
+++++++++++++++++++++++++++++++
|C|u|r|s|o| |d|e| |P|y|t|h|o|n|
+++++++++++++++++++++++++++++++
 0 1 2 3 4 5 6 7 8 9 10  ... 14
'''

# Cadeia de caracteres
frase = 'Curso de Python'

# Exibindo
print(frase)

# Fatiamento - Fatiando uma letra
print(frase[3])

# Fatiamento - Fatiamento do indice nove até o 15, mas o Python exibe até o 14
print(frase[9:15])

# Fatiamento - Fatiamento do indice nove até o 15, mas o Python exibe até o 14
# pulando de 2 em 2
print(frase[9:15:2])

# Fatiamento - Fatiando e não exibindo os primeiros nove caracteres
print(frase[:5])

# Fatiamento - Fatiando e não exibindo os primeiros nove caracteres
print(frase[9:])

# Fatiamento - Fatiando do primeiro até o 10 (15-5) e exibindo até o nono caracter
print(frase[:-5])

# Fatiamento - Fatiando do sexto caracter até o final, pulando de 2 em 2
print(frase[6::2])
