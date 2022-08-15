'''
Estruturas de Repetição - While, Break e Continue
'''

num = 1
pares = 0
impares = 0

while num != 0:
    num = int(input('Digite um número: '))

    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print('Pares {}\nÍmpares {}'.format(pares, impares))

# while True:
#     num = int(input('Digite um número: '))
#
#     if num % 2 == 0:
#         pares += 1
#     else:
#         impares += 1
#
#     if num == 0:
#         break
#
# print('Pares {}\nÍmpares {}'.format(pares, impares))



# x = 0
# while x <= 10:
#     x += 1
#
#     if x % 2 == 0:
#         continue
#
#     if x > 7:
#         break
#
#     print(x)