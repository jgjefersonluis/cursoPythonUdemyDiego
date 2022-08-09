'''
Exercício 1
---
Faça um script que o computador sorteia um número inteiro entre 0 e 5.
Depois o usuário deve tentar adivinhar o número escolhido pelo computador.
No final, o script deverá escrever na tela se o usuário venceu ou perdeu,
ou seja, se ele acertou ou não o número sorteado pelo computador.
'''
import random

numeroSorteado = random.randint(0,5)

numeroUsuario = int(input('Qual o número sorteado (entre 0 e 5)?'))

if numeroUsuario == numeroSorteado:
    print('Você acertou! O número {} é o mesmo que o sorteado {}'.format(numeroUsuario, numeroSorteado))
else:
    print('Você errou! O número {} não é o sorteado {}'.format(numeroUsuario, numeroSorteado))

