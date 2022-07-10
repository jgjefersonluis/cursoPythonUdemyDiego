'''
Exercícios de Python para a assimilação do conteúdo já apresentado
Curso de Python

Diego M. Rodrigues

Exercício 2
---
Receba do usuário uma informação do teclado.
Exiba o tipo primitivo dessa informação recebida e depois todas
as possíveis informações sobre ela.
'''

# Recebendo o valor do usuário
valor = input('Digite algo: ')

# Realizando os testes e exibindo as informações
print('Numeric:',valor.isnumeric())
print('Alpha: ',valor.isalpha())
print('AlphaNum: ',valor.isalnum())
print('Decimal: ',valor.isdecimal())
print('Digit: ',valor.isdigit())
print('Lower: ',valor.islower())
print('Upper: ',valor.isupper())
print('Printable: ',valor.isprintable())
print('Space: ',valor.isspace())
print('Title: ',valor.istitle())