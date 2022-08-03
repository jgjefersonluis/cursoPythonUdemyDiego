'''
Exercício 2
---
Leia um ângulo do usuário final, depois exiba na tela o seno, o cosseno e a tangente.
'''
# Importando o módulo math
import math

# Recebendo o ângulo
angulo = float(input('Angulo em graus: '))

# Convertendo o angulo para radianos, sendo essa a medida utilizada nas funções
# de seno, cosseno e tangente
anguloRadianos = math.radians(angulo)

# Calculando
seno = math.sin(anguloRadianos)
cosseno = math.cos(anguloRadianos)
tangente = math.tan(anguloRadianos)

# Mostrando na tela
print('Angulo {}'.format(angulo))
print('Seno {:.2f} - Cosseno {:.2f} - Tangente {:.2f}'.format(seno, cosseno, tangente))

