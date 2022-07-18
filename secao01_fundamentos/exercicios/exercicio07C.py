'''
Exercício 7
---
Leia a altura e a largura de uma parede.
Exiba a área da parede e a quantidade de tinta necessária para pintá-la,
considerando que 1 litro de tinta pinta uma área de 3 metros quadrados.
'''

# Entrada da altura e da largura
alt = float(input('Altura da parede: '))
lar = float(input('Largura da parede: '))

# Calculando a área e a quantidade de tinta
area = alt * lar
tinta = area/3

# Exibindo
print('A parede possui uma área de {} metros quadrados.'.format(area))
print('Você precisa de {:.1f} litros de tinta para pintar a parede.'.format(tinta))
