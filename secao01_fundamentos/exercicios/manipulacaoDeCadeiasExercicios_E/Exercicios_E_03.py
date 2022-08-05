'''
Exercício 3
---
O usuário entra com o nome de uma cidade.
Analisar se o nome da cidade começa ou não com SÃO
'''

# Recebendo a cidado do usuário como uma string
# Eliminando os espaços inúteis digitaos
cidade = str(input('Cidade: ')).strip()

# Separando os 3 primeiros caracteres, depois convertendo para maiúscuco
# e finalmente verificado se o resultado é igual a SÃO
print(cidade[:3].upper() == 'SÃO')
#print(cidade[:3])