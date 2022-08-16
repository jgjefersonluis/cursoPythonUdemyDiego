'''
Exercício 4
---
Solicite as 2 notas de História de um aluno, depois calcule a média final dele.
De acordo com a média, exiba:
Média abaixo de 5 - Reprovado.
Média entre 5 e 6.9 - Em Recuperação.
Média maior que 7 - Aprovado.
'''

nota1 = float(input('Nota mensal: '))
nota2 = float(input('Nota bimestral: '))

media = (nota1 + nota2) / 2

if media < 5:
    print('Reprovado - Média {:.1f}'.format(media))
elif media >= 5 and media < 7:
    print('Em recuperação - Média {:.1f}'.format(media))
else:
    print('Aprovado - Média {:.1f}'.format(media))
