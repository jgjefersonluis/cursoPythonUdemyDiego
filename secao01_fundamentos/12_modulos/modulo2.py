# Importando APENAS as funções necessárias do módulo math
from math import sqrt, ceil, floor, pow

# Recebendo o valor do usuário
num = int(input('Digite um número: '))

# Calculando a raiz quadrada com a função sqrt do math
# Agora, não utilizamos o .math
raiz = sqrt(num)

print('Número {} - Raiz {}'.format(num, raiz))

# Realizando arredondamentos com as funções ceil e floor do math
# Não utilizamos o .math
print('Número {} - Raiz {}'.format(num, ceil(raiz)))
print('Número {} - Raiz {}'.format(num, floor(raiz)))

# Calculando a potência utilizando o função pow do math
# Não utilizamos o .math
print('Potência: {}'.format(pow(2,3)))
