'''
Condições Aninhadas

            Visitante
               |
   +-----------+--------------
   |                          |
   |                          |
  <18                        >18
   |                          |
  Não               +---------+---------+
 entra              |         |         |
                    21        60       +60
                    |         |         |
                  Refri.   Cerveja     Água
                            Vodka
'''

idade = int(input('Qual é a sua idade?'))

if idade < 18:
    print('Apenas pessoas com 18 anos ou mais podem entrar.')
else:
    print('Bem vindo ao Bar!')

    if idade <= 21:
        print('Você pode solicitar refrigerantes')
    elif idade > 21 and idade <= 60:
        print('Voce pode solicitar cerveja ou vodka')
    else:
        print('Você pode solicitar água')

