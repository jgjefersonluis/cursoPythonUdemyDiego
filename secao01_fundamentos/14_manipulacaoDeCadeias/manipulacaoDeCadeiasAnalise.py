'''
Manipular as Cadeias de Caracteres - ANÁLISE
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

# Tamanho da cadeia
print(len(frase))

# Contar quantas vezes aparece a letra o minúscula
print(frase.count('o'))

# Contar quantas vezes aparece a letra o minúscula, mas realizar antes um fatiamento
# do caracter 0 até o 4, já que o Python ignora o último índice que colocamos, o 5
print(frase.count('o', 0, 5))

# Localizar a posição que começa 'de' na frase
print(frase.find('de'))

# Localizar a posição que começa 'PHP' na frase
# Como não existe PHP na frase, o retorno é -1
print(frase.find('PHP'))

# Usando o operador in para descobrir se 'Curso' está ou não está na frase
# O retorno do in é True ou False
print('Curso' in frase)
print('PHP' in frase)
