'''
Exercício 4
---
Verifique se o nome de uma pessoa possui SILVA nele.
'''

# Recebendo o nome do usuário como uma string
nome = str(input('Seu nome: '))

# Verificando se o nome possui Silva
print('silva' in nome.lower())
