'''
Exercício 5
---
Nesse programa, o usuário irá entrar com uma frase, depois você mostra:
Quantas vezes apareceu a letra A
Em que posição ela aparece pela primeira vez
Em que posição ela aparece pela última vez
'''
# Entrada da frase pelo usuário
frase = str(input('Digite uma frase: '))

# Quantas vezes apareceu a letra A
print('Quantas vezes apareceu a letra A: {}'.format(frase.lower().count('a')))

# Em que posição ela aparece pela primeira vez
print('Aparece pela primeira vez: {}'.format(frase.lower().find('a')))

# Em que posição ela aparece pela última vez
print('Aparece pela última vez: {}'.format(frase.lower().rfind('a')))