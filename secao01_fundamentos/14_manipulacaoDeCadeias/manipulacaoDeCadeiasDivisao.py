'''
Manipular as Cadeias de Caracteres - DIVISÃO
'''

'''
Cadeia de caracteres armazenada na memória com seus índices
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|C|u|r|s|o| |d|e| |P|y|t|h|o|n| |e| |B|a|n|c|o| |d|e| |D|a|d|o|s| 
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
 0 1 2 3 4 5 6 7 8 9 10  ...                                   31
'''

# Cadeia de caracteres
frase = 'Curso de Python e Banco de Dados'

# Dividindo com a função split(), usando o espaço como ponto de divisão
# O retorno do split é uma Lista
print(frase.split())

# Armazenando a lista da divisão em uma variável
palavras = frase.split()
print(palavras)

# Exibindo o ítem com índice 2 da lista
print(palavras[2])

# Armazenando o ítem 2 da lista em uma variável do tipo string
linguagem = palavras[2]
print(linguagem)

# Criando uma nova cadeia de caracteres, onde não temos espaços, e sim, vírgulas
frase2 = '1,2,3,4,5'

# Realizando o split com as vírgulas
print(frase2.split(','))

# Limitando a divisão em uma única ocorrência
print(frase2.split(',', maxsplit=2))

#----------
# Junção
#__________

# Juntando a lista palavras com o join(), utilizando o traço como o elemento de junção
frase3 = '-'.join(palavras)
print(frase3)

# Juntando a lista palavras com o join(), utilizando o espaço como o elemento de junção
frase4 = ''.join(palavras)
print(frase4)
