# Importando o módulo math
import math

# Recebendo o valor do usuário
num = int(input('Digite um número: '))

# Calculando a raiz quadrada com a função sqrt do math
raiz = math.sqrt(num)

print('Número {} - Raiz {}'.format(num, raiz))

# Realizando arredondamentos com as funções ceil e floor do math
print('Número {} - Raiz {}'.format(num, math.ceil(raiz)))
print('Número {} - Raiz {}'.format(num, math.floor(raiz)))

