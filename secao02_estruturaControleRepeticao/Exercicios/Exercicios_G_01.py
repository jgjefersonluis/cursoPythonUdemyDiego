'''
Exercícios de Python para a assimilação do conteúdo já apresentado
---
Faça um script que o computador sorteia um número inteiro entre 0 e 5.
Depois o usuário deve tentar adivinhar o número escolhido pelo computador.
No final, o script deverá escrever na tela se o usuário venceu ou perdeu,
ou seja, se ele acertou ou não o número sorteado pelo computador.
'''
import random

numeroSorteado = random.randint(0, 5)

numeroUsuario = int(input('Qual o número sorteado (entre 0 e 5)? '))

if numeroUsuario == numeroSorteado:
    print('Você \033[1;32macertou\033[m! '
          'O número \033[4m{}\033[m é o mesmo que o sorteado \033[4m{}\033[m!'.format(numeroUsuario,
                                                                                         numeroSorteado))
else:
    print('Você \033[1;31merrou\033[m! '
          'O número \033[4m{}\033[m não é o sorteado \033[4m{}\033[m!'.format(numeroUsuario,
                                                                                numeroSorteado))

