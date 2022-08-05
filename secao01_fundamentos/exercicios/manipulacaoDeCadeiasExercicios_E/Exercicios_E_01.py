'''
Exercício 1
---
Crie um script que leia o nome completo de uma pessoa, depois mostre:
O nome com todas as letras maiúsculas
O nome com todas as letras minúsculas
Quantas letras tem o nome sem considerar os espaços?
Quantas letras possui o primeiro nome?
'''

# Recebendo o nome completo
nome = str(input('Qual é o seu nome completo:'))

# Letras maiúsculas
print(nome.upper())

# Letras minúsculas
print(nome.lower())

# Letras que o nome possui sem espaços
print(nome.replace('',''))
print(len(nome.replace('','')))

# Letras no primeiro nome
nomeQuebrado = nome.split()
print(nomeQuebrado)
print(len(nomeQuebrado[0]))
