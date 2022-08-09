'''
Cores no Terminal do Python utilizando o padrão ANSI
'''

'''
\033[m
\033[ESTILO;COR_TEXTO;COR_FUNDOm

Estilo		    Texto		    Fundo
--------------  --------------  ----------------
0 Nada		    30 Branco	    40 Branco
1 Negrito	    31 Vermelho	    41 Vermelho
4 Sublinhado	32 Verde	    42 Verde
7 Inverter	    33 Amarelo	    43 Amarelo
		        34 Azul		    44 Azul
		        35 Magenta	    45 Magenta
		        36 Ciano	    46 Ciano
		        37 Cinza	    47 Cinza
'''

# Exemplos de cores
print('\033[0;31;47mCursos de Python\033[m')
print('\033[4;30;44mCursos de Python\033[m')
print('\033[1;37;44mCursos de Python\033[m')

# Separando a cor no print usando o .format()
n = 10
print('O número escolhido foi {} {} {} '.format('\033[1;31m', n, '\033[m'))
# print('O número escolhido foi \033[1;31m{}\033[m'.format(n))

